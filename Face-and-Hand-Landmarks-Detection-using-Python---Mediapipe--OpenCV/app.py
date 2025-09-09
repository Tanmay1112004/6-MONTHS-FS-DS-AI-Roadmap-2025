# app.py
import os
import io
import time
from datetime import datetime
import tempfile

import streamlit as st
import numpy as np
import cv2

from detector import FaceHandDetector

st.set_page_config(page_title="Face & Hand Landmarks", layout="wide")
st.title("🎭 Face & Hand Landmarks Detection — Mediapipe + OpenCV")

# Sidebar
st.sidebar.header("Settings")
mode = st.sidebar.radio("Input source", ["Browser webcam (snapshot)", "Upload image/video", "Server camera (experimental)"])
draw_face = st.sidebar.checkbox("Show Face Landmarks", True)
draw_hands = st.sidebar.checkbox("Show Hand Landmarks", True)

if "snapshots_dir" not in st.session_state:
    st.session_state.snapshots_dir = "snapshots"
    os.makedirs(st.session_state.snapshots_dir, exist_ok=True)

detector = FaceHandDetector(min_detection_confidence=0.5, min_tracking_confidence=0.5)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input")
    if mode == "Browser webcam (snapshot)":
        st.info("This uses your browser camera — works from Codespaces or local browser instantly.")
        camera_file = st.camera_input("Take a snapshot")
        if camera_file:
            bytes_data = camera_file.getvalue()
            processed = detector.process_bytes(bytes_data, draw_face=draw_face, draw_hands=draw_hands)
            st.image(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB), caption="Processed snapshot", use_column_width=True)
            # Save snapshot
            fname = f"{st.session_state.snapshots_dir}/snap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            cv2.imwrite(fname, processed)
            st.markdown(f"Saved snapshot: `{fname}`")
            # Provide download
            is_success, buffer = cv2.imencode(".png", processed)
            st.download_button("Download PNG", buffer.tobytes(), file_name="processed_snapshot.png")

    elif mode == "Upload image/video":
        upload = st.file_uploader("Upload image or short video (mp4/mov)", type=["png","jpg","jpeg","mp4","mov","avi"])
        if upload:
            b = upload.read()
            # If image
            if upload.type.startswith("image"):
                processed = detector.process_bytes(b, draw_face=draw_face, draw_hands=draw_hands)
                st.image(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB), caption="Processed image", use_column_width=True)
                is_success, buffer = cv2.imencode(".png", processed)
                st.download_button("Download PNG", buffer.tobytes(), file_name="processed_image.png")
            else:
                # simple: process first frame of video and show
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
                    tmp.write(b)
                    tmp_path = tmp.name
                cap = cv2.VideoCapture(tmp_path)
                ret, frame = cap.read()
                if not ret:
                    st.error("Could not read uploaded video.")
                else:
                    processed = detector.process_frame(frame, draw_face=draw_face, draw_hands=draw_hands)
                    st.image(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB), caption="Processed first frame")
                    is_success, buffer = cv2.imencode(".png", processed)
                    st.download_button("Download first frame PNG", buffer.tobytes(), file_name="processed_video_frame.png")
                cap.release()

    else:  # Server camera (experimental)
        st.warning("Server camera will only work if the container/host exposes a camera device to this environment.")
        start = st.button("Start server camera")
        stop = st.button("Stop server camera")
        if start:
            st.session_state["server_cam_running"] = True
        if stop:
            st.session_state["server_cam_running"] = False

        if st.session_state.get("server_cam_running", False):
            FRAME_WINDOW = st.image([])
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                st.error("Server camera not available (no /dev/video or access). Try Browser webcam mode or run locally.")
            else:
                try:
                    while st.session_state.get("server_cam_running", True):
                        ret, frame = cap.read()
                        if not ret:
                            st.warning("No frame from server camera.")
                            break
                        processed = detector.process_frame(frame, draw_face=draw_face, draw_hands=draw_hands)
                        FRAME_WINDOW.image(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
                        # small sleep so CPU doesn't spike
                        time.sleep(0.02)
                except st.script_runner.StopException:
                    pass
                finally:
                    cap.release()

with col2:
    st.subheader("Info & Tips")
    st.markdown("""
    - Use **Browser webcam** to take snapshots directly from your local camera (best for Codespaces).
    - **Server camera** is experimental — Codespaces generally can't see your laptop webcam unless forwarded. Run locally for best realtime results.
    - This app supports **Python 3.10–3.11** only (Mediapipe wheels are not guaranteed for Python 3.12+).
    """)
    st.markdown("### Snapshots folder")
    st.text(st.session_state.snapshots_dir)
    if os.path.exists(st.session_state.snapshots_dir):
        files = sorted(os.listdir(st.session_state.snapshots_dir), reverse=True)[:10]
        for f in files:
            st.write(f"- {f}")

st.markdown("---")
st.caption("Built with Tanmay — Mediapipe + OpenCV + Streamlit")
