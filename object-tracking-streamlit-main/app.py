import cv2
import tempfile
import streamlit as st
from tracker import EuclideanDistTracker
import numpy as np
import os
from datetime import datetime

# ------------------------------
# Streamlit Page Config
# ------------------------------
st.set_page_config(page_title="🚗 Object Tracking App", layout="wide")
st.title("🚗 Real-time Object Tracking with OpenCV + Streamlit")
st.markdown("Upload a video, choose options, and get a tracked output in seconds!")

# ------------------------------
# Sidebar Controls
# ------------------------------
st.sidebar.header("⚙️ Settings")
resize_width = st.sidebar.selectbox("Resize Width", [320, 480, 640], index=2)
frame_skip = st.sidebar.slider("Frame Skip (higher = faster)", 1, 10, 3)
min_area = st.sidebar.slider("Min Object Area", 50, 500, 100)

# ------------------------------
# File Upload
# ------------------------------
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    # Preview original video
    st.video(video_path)

    # Process button
    if st.button("🚀 Start Processing"):
        st.info("Processing video... please wait ⏳")
        progress = st.progress(0)

        # Initialize tracker and detector
        tracker = EuclideanDistTracker()
        object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

        cap = cv2.VideoCapture(video_path)

        # Output file
        output_path = f"output_{datetime.now().strftime('%H%M%S')}.mp4"
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_path, fourcc, 20.0, (resize_width, int(resize_width * 0.5625)))

        total_objects = 0
        frame_count = 0
        processed_frames = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1

            # Skip frames for speed
            if frame_count % frame_skip != 0:
                continue

            # Resize frame
            frame = cv2.resize(frame, (resize_width, int(resize_width * 0.5625)))

            # Region of interest (here using whole frame)
            roi = frame

            # Object detection
            mask = object_detector.apply(roi)
            _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            detections = []
            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > min_area:
                    x, y, w, h = cv2.boundingRect(cnt)
                    detections.append([x, y, w, h])

            # Object Tracking
            boxes_ids = tracker.update(detections)
            for box_id in boxes_ids:
                x, y, w, h, id = box_id
                cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
                total_objects = max(total_objects, id + 1)

            # Write processed frame
            out.write(frame)
            processed_frames += 1

            # Update progress
            progress.progress(min(1.0, frame_count / cap.get(cv2.CAP_PROP_FRAME_COUNT)))

        cap.release()
        out.release()

        # Results
        st.success("✅ Processing Complete!")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Frames", str(frame_count))
        col2.metric("Processed Frames", str(processed_frames))
        col3.metric("Objects Tracked", str(total_objects))

        # Show processed video
        st.subheader("🎥 Processed Output")
        st.video(output_path)

        # Download button
        with open(output_path, "rb") as f:
            st.download_button("⬇️ Download Processed Video", f, file_name="tracked_output.mp4")
