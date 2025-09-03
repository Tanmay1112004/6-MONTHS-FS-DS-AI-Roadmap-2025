# 👀 Face & Eye Detection App

A simple Face & Eye Detection web app built with **OpenCV**, **Haar Cascades**, and **Gradio**.  
It works in **Google Colab** (no local setup needed) and allows you to either:

- 📂 Upload an image  
- 🎥 Capture directly from your webcam  

Detected faces are highlighted with **blue rectangles**, and eyes with **green rectangles**.

---

## 🚀 Features
- Face detection using `haarcascade_frontalface_default.xml`
- Eye detection using `haarcascade_eye.xml`
- Upload image OR capture live from webcam
- Built with [Gradio](https://gradio.app) for a clean web-based frontend
- Colab-ready (no installation headaches)

---

## 🛠️ Installation

Clone the repo:
```bash
git clone https://github.com/your-username/face-eye-detection-app.git
cd face-eye-detection-app
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run in Google Colab

Copy & paste this into a Colab notebook:

```python
!pip install gradio opencv-python-headless matplotlib

import cv2
import numpy as np
import gradio as gr

def detect_faces_and_eyes(image):
    if image is None:
        return None
    img = np.array(image.convert("RGB"))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb

with gr.Blocks() as demo:
    gr.Markdown("## 👀 Face & Eye Detection App\nUpload an image or take a live webcam snapshot.")

    with gr.Row():
        inp = gr.Image(type="pil", label="Upload Image", sources=["upload"])
        cam = gr.Image(type="pil", label="Or Capture from Webcam", sources=["webcam"])

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
matplotlib
numpy
```

---

## 📷 Example Output

![example](https://opencv.org/wp-content/uploads/2021/11/opencv-logo.png)
*(Replace with your own screenshot of detection results)*

---

## 🏗️ Future Enhancements

* Save & download detected images
* Multiple face detection
* Support for other detectors (DNN, YOLO, Mediapipe)

---

## 📜 License

MIT License © 2025

```
