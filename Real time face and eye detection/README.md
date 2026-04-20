# 👀 Face & Eye Detection App

A professional, lightweight Computer Vision web application built using **OpenCV**, **Haar Cascade classifiers**, and **Gradio**.

This project demonstrates practical implementation of classical CV techniques in a deployable, user-friendly interface — fully compatible with **Google Colab** (no local setup required).

---

## 📌 Project Overview

The **Face & Eye Detection App** detects:

* 🟦 **Faces** (highlighted with blue bounding boxes)
* 🟩 **Eyes** (highlighted with green bounding boxes inside detected faces)

Users can:

* 📂 Upload an image
* 🎥 Capture directly from their webcam

This project showcases applied computer vision fundamentals, image preprocessing, object detection pipelines, and web-based ML deployment.

---

## 🧠 Technical Highlights

* Haar Cascade–based face detection
* Eye detection within face ROI (Region of Interest)
* Real-time image preprocessing (RGB ↔ BGR conversion)
* Gradio-powered interactive web interface
* Fully functional in Google Colab
* Minimal dependencies & lightweight deployment

---

## 🛠 Tech Stack

| Layer                | Technology    |
| -------------------- | ------------- |
| Computer Vision      | OpenCV        |
| Detection Model      | Haar Cascades |
| Frontend Interface   | Gradio        |
| Numerical Processing | NumPy         |
| Deployment           | Google Colab  |

---

## 🚀 Key Features

* Face detection using `haarcascade_frontalface_default.xml`
* Eye detection using `haarcascade_eye.xml`
* Upload or webcam capture support
* Clean web-based UI via Gradio Blocks
* Colab-ready execution
* Lightweight & beginner-friendly architecture

---

## ▶️ Quick Start (Local Setup)

### Clone Repository

```bash
git clone https://github.com/your-username/face-eye-detection-app.git
cd face-eye-detection-app
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ☁️ Run Instantly in Google Colab

Install dependencies:

```python
!pip install gradio opencv-python-headless matplotlib numpy
```

Then use the detection function and Gradio interface:

```python
import cv2
import numpy as np
import gradio as gr

def detect_faces_and_eyes(image):
    if image is None:
        return None
    img = np.array(image.convert("RGB"))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye.xml"
    )

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex+ew, ey+eh),
                (0, 255, 0),
                2
            )

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb


with gr.Blocks() as demo:
    gr.Markdown(
        "## 👀 Face & Eye Detection App\n"
        "Upload an image or capture from webcam."
    )

    with gr.Row():
        inp = gr.Image(type="pil", label="Upload Image", sources=["upload"])
        cam = gr.Image(type="pil", label="Capture from Webcam", sources=["webcam"])

    run_btn = gr.Button("Run Detection", variant="primary")
    out_img = gr.Image(type="numpy", label="Detection Result")

    run_btn.click(fn=detect_faces_and_eyes, inputs=inp, outputs=out_img)
    run_btn.click(fn=detect_faces_and_eyes, inputs=cam, outputs=out_img)

demo.launch(debug=True, share=True)
```

---

## 📦 Requirements

```
opencv-python-headless
gradio
numpy
matplotlib
```

---

## 📷 Example Output


Detected faces are marked in **blue**, and eyes are marked in **green** within the detected face region.

---

## 🏗 Architecture Overview

```
Input Image
    ↓
Preprocessing (RGB → BGR → Grayscale)
    ↓
Face Detection (Haar Cascade)
    ↓
Eye Detection within ROI
    ↓
Bounding Box Rendering
    ↓
Output via Gradio Interface
```

The modular structure makes it easy to extend to more advanced detectors like DNN or deep learning models.

---

## 🔮 Future Enhancements

* Save & download processed images
* Support for multiple face tracking
* Upgrade to DNN-based detection
* Integration with YOLO / Mediapipe
* Real-time video stream processing

---

## 🎯 Why This Project Matters

This project demonstrates:

✔ Applied Computer Vision fundamentals
✔ Object detection pipeline implementation
✔ Clean UI integration for ML models
✔ Rapid prototyping & deployment
✔ Practical understanding of OpenCV internals

It serves as a strong foundational CV project suitable for internships, ML roles, and software engineering portfolios.

---

## 📜 License

MIT License © 2026

---
