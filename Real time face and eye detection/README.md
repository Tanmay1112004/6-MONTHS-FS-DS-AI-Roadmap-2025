# 👀 Face & Eye Detection App — Real-Time Computer Vision System

<p align="center">
  <b>Detect faces and eyes instantly using classical Computer Vision techniques</b><br>
  Built with OpenCV + Gradio for fast, lightweight, and deployable CV applications
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/UI-Gradio-red?style=flat-square"/>
  <img src="https://img.shields.io/badge/Focus-Object%20Detection-orange?style=flat-square"/>
</p>

---

## 💡 What This Project Does

This application detects:

* 🟦 Faces (bounding boxes)
* 🟩 Eyes (within detected face regions)

👉 All in real-time through an interactive web interface.

---

## Demo Images 

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Real%20time%20face%20and%20eye%20detection/screenshots/Screenshot%202025-09-03%20192351.png)

---

## 🚨 Problem Statement

Many CV projects:

* Focus only on deep learning
* Ignore classical techniques
* Lack deployable interfaces

👉 Result: No understanding of fundamentals or real-world usability

---

## 🎯 Solution

A lightweight **computer vision detection system** that:

✅ Uses efficient classical algorithms (Haar Cascades)
✅ Processes images in real-time
✅ Provides an interactive UI for usability
✅ Works seamlessly on low-resource systems

---

## ⚡ Key Features

### 👁️ Face Detection

* Haar Cascade (`frontalface_default`)
* Accurate bounding box detection

### 👀 Eye Detection (ROI-Based)

* Detects eyes only within face region
* Improves efficiency and reduces false positives

### ⚡ Real-Time Processing

* Fast detection without GPU
* Optimized preprocessing pipeline

### 💻 Interactive UI

* Upload images or capture via webcam
* Built with Gradio for instant feedback

---

## 🧠 Why This Project Stands Out (Recruiter POV)

Most candidates:
👉 Jump straight to deep learning

This project:

✅ Demonstrates **core CV fundamentals**
✅ Shows understanding of **detection pipelines**
✅ Combines **ML + UI deployment**
✅ Focuses on **efficiency & real-world usability**

👉 Translation: *You understand how CV systems actually work under the hood.*

---

## 🧬 Detection Pipeline

```id="cvflow22"
Input Image
   │
   ▼
Color Conversion (RGB → BGR → Grayscale)
   │
   ▼
Face Detection (Haar Cascade)
   │
   ▼
Region of Interest (ROI Extraction)
   │
   ▼
Eye Detection within ROI
   │
   ▼
Bounding Box Rendering
   │
   ▼
Gradio UI Output
```

---

## 🛠 Tech Stack

| Layer           | Technology    |
| --------------- | ------------- |
| Computer Vision | OpenCV        |
| Detection Model | Haar Cascades |
| UI              | Gradio        |
| Processing      | NumPy         |
| Deployment      | Google Colab  |

---

## 🚀 Quick Start

```bash id="runface1"
git clone https://github.com/Tanmay112004/face-eye-detection-app.git
cd face-eye-detection-app
pip install -r requirements.txt
python app.py
```

---

## ☁️ Run on Google Colab

```python id="colabface1"
!pip install gradio opencv-python-headless numpy
import app
```

---

## 📊 Example Output

* Faces → **Blue bounding boxes**
* Eyes → **Green bounding boxes (inside faces)**

---

## 🎯 Real-World Applications

* Face detection systems
* Attendance systems
* Surveillance applications
* Preprocessing for face recognition

---

## 📈 What This Project Demonstrates

* Classical computer vision fundamentals
* Object detection pipeline design
* Image preprocessing techniques
* ML + UI integration
* Deployment-ready applications

---

## 🔮 Future Enhancements

* [ ] DNN-based face detection (OpenCV DNN / YOLO)
* [ ] Real-time video streaming
* [ ] Face recognition integration
* [ ] Multi-face tracking
* [ ] Performance optimization

---

## 🤝 Contributing

```bash id="contri_face1"
git checkout -b feature/improvement
git commit -m "Enhancement added"
git push origin feature/improvement
```

---

## ⭐ Support

If you found this useful:

* ⭐ Star the repo
* 🍴 Fork it
* 🚀 Use it in your projects

---

## 👨‍💻 Developer Mindset

**From pixels → detection → usable CV system**

---

## 🔥 Final Thought

Deep learning gets attention.

👉 But strong fundamentals build great engineers.

---

<p align="center">
  👀 <b>See smarter. Detect faster.</b>
</p>
