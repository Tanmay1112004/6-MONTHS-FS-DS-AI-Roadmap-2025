"""
Streamlit app: 3D Object Detection (MediaPipe Objectron)
Features:
 - Image URL or file upload
 - Models: Cup, Chair, Shoe, Camera
 - Colored 3D bounding boxes & landmarks (visible on white backgrounds)
 - Rotation & Translation displayed as tables
 - CSV download of pose data
 - Optional image resizing for large images
"""

import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image
import urllib.request
import io
import pandas as pd
from typing import Tuple, List, Dict

# MediaPipe setup
mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

st.set_page_config(page_title="Objectron 3D Detection", layout="centered")
st.title("3D Object Detection — MediaPipe Objectron")
st.write("Detect 3D bounding boxes (Objectron). Works best with cups, chairs, shoes, cameras.")

# UI controls
model_name = st.selectbox("Model", ["Cup", "Chair", "Shoe", "Camera"], index=1)
min_conf = st.slider("Min detection confidence", 0.1, 0.9, 0.3, 0.05)
input_mode = st.radio("Input", ("Image URL", "Upload Image"))
resize_enabled = st.checkbox("Auto-resize large images (faster)", value=True)
max_dim = st.number_input("Max image dimension when resizing (px)", min_value=256, max_value=2000, value=1000, step=100)

EXAMPLE_URL = "https://goodstock.photos/wp-content/uploads/2018/01/Laptop-Coffee-Mug-on-Table.jpg"

def url_to_array(url: str, timeout=12) -> np.ndarray:
    try:
        resp = urllib.request.urlopen(url, timeout=timeout)
        arr = np.asarray(bytearray(resp.read()), dtype=np.uint8)
        bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        return rgb
    except Exception as e:
        return None

def file_to_array(uploaded_file) -> np.ndarray:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        return np.array(image)
    except Exception:
        return None

def resize_if_needed(img: np.ndarray, max_dim_px: int) -> np.ndarray:
    h, w = img.shape[:2]
    if max(h, w) <= max_dim_px:
        return img
    scale = max_dim_px / max(h, w)
    new_w = int(w * scale)
    new_h = int(h * scale)
    return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

def detect_and_annotate(img_rgb: np.ndarray, model="Cup", min_detection_confidence=0.3) -> Tuple[np.ndarray, List[Dict]]:
    annotated = img_rgb.copy()
    objs_info = []
    # Use context manager so objectron resources are released
    with mp_objectron.Objectron(
        static_image_mode=True,
        max_num_objects=5,
        min_detection_confidence=min_detection_confidence,
        model_name=model
    ) as objectron:
        results = objectron.process(img_rgb)
        if not results.detected_objects:
            return None, None
        for detected in results.detected_objects:
            # Draw landmarks (points) in green and connections (box) in blue
            landmark_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3)
            connection_spec = mp_drawing.DrawingSpec(color=(0, 102, 255), thickness=2)  # bluish
            mp_drawing.draw_landmarks(
                annotated,
                detected.landmarks_2d,
                mp_objectron.BOX_CONNECTIONS,
                landmark_drawing_spec=landmark_spec,
                connection_drawing_spec=connection_spec
            )
            # Draw axis (X=red, Y=green, Z=blue by default) — they are visible on bright backgrounds
            mp_drawing.draw_axis(
                annotated,
                detected.rotation,
                detected.translation
            )

            # Optionally draw an extra rectangle around 2D landmarks for extra visibility (white outline + colored inner)
            try:
                # compute bounding rect around landmarks_2d
                pts = np.array([[int(p.x * annotated.shape[1]), int(p.y * annotated.shape[0])] for p in detected.landmarks_2d])
                x, y, w, h = cv2.boundingRect(pts)
                # draw white thicker rectangle for contrast, then colored rectangle
                cv2.rectangle(annotated, (x-3, y-3), (x+w+3, y+h+3), (255,255,255), thickness=6)  # white highlight
                cv2.rectangle(annotated, (x-1, y-1), (x+w+1, y+h+1), (0, 102, 255), thickness=2)  # colored
            except Exception:
                pass

            objs_info.append({
                "rotation": detected.rotation.tolist(),
                "translation": detected.translation.tolist()
            })
    return annotated, objs_info

def pose_tables_and_csv(infos: List[Dict]):
    all_frames = []
    st.subheader("Pose Information")
    for i, obj in enumerate(infos, start=1):
        st.markdown(f"#### Object {i}")
        rotation_matrix = pd.DataFrame(obj["rotation"], columns=["X", "Y", "Z"], index=["R1", "R2", "R3"])
        st.markdown("**Rotation Matrix (3×3):**")
        st.table(rotation_matrix)

        translation_vector = pd.DataFrame(obj["translation"], columns=["Value"], index=["Tx", "Ty", "Tz"])
        st.markdown("**Translation Vector (3×1):**")
        st.table(translation_vector)

        # rename indices to avoid duplicates in CSV
        rot = rotation_matrix.copy()
        rot.index = [f"Obj{i}_R1", f"Obj{i}_R2", f"Obj{i}_R3"]
        trans = translation_vector.copy()
        trans.index = [f"Obj{i}_Tx", f"Obj{i}_Ty", f"Obj{i}_Tz"]
        all_frames.extend([rot, trans])

    # Create CSV and provide download button
    if all_frames:
        csv_buf = io.StringIO()
        pd.concat(all_frames).to_csv(csv_buf)
        st.download_button(
            "📥 Download Pose Data (CSV)",
            csv_buf.getvalue(),
            file_name="pose_data.csv",
            mime="text/csv"
        )

# Main UI flow
if input_mode == "Image URL":
    url = st.text_input("Image URL", value=EXAMPLE_URL)
    if st.button("Detect from URL"):
        if not url:
            st.error("Please paste a valid image URL.")
        else:
            st.info("Loading image...")
            img = url_to_array(url)
            if img is None:
                st.error("Could not load image from URL.")
            else:
                if resize_enabled:
                    img = resize_if_needed(img, max_dim)
                with st.spinner("Detecting..."):
                    annotated, infos = detect_and_annotate(img, model=model_name, min_detection_confidence=min_conf)
                if annotated is None:
                    st.warning("No objects detected. Showing original image.")
                    st.image(img, use_container_width=True)
                else:
                    st.success(f"Detected {len(infos)} object(s).")
                    st.image(annotated, use_container_width=True)
                    pose_tables_and_csv(infos)

else:  # Upload Image
    uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded is not None:
        img = file_to_array(uploaded)
        if img is None:
            st.error("Failed to read uploaded image.")
        else:
            if resize_enabled:
                img = resize_if_needed(img, max_dim)
            with st.spinner("Detecting..."):
                annotated, infos = detect_and_annotate(img, model=model_name, min_detection_confidence=min_conf)
            if annotated is None:
                st.warning("No objects detected. Showing original image.")
                st.image(img, use_container_width=True)
            else:
                st.success(f"Detected {len(infos)} object(s).")
                st.image(annotated, use_container_width=True)
                pose_tables_and_csv(infos)

st.info("If you see import errors about libGL, ensure the devcontainer Dockerfile or the Codespace has libgl1 installed.")
