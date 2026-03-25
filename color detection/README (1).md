# 🎨 Color Detection Engine — OpenCV + Gradio CV Application

A real-time computer vision system for **color segmentation and object localization**, powered by OpenCV and delivered through an interactive Gradio web interface.

This project demonstrates a classic yet highly practical CV pipeline using **HSV thresholding**, contour detection, and spatial bounding — applicable to robotics, quality inspection, AR systems, and more.

---

## 🖼️ Supported Inputs

📷 Static image upload
🎥 Real-time webcam stream

![IMG](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/color%20detection/screenshots/Screenshot%202025-09-04%20142530.png)


---

## ✨ Project Highlights

🎯 Real-time color-based object detection
🌈 Lighting-robust HSV segmentation
📦 Bounding box localization
📷 Supports images + webcam input
🌐 Deployable via browser interface
☁️ Google Colab compatible

---

## 🧠 How It Works

The system detects objects based on chrominance rather than shape or texture.

### Processing Pipeline

1️⃣ **Frame Acquisition** — Image upload or webcam capture
2️⃣ **Color Space Conversion** — BGR → HSV
3️⃣ **Threshold Masking** — Isolate target color ranges
4️⃣ **Contour Extraction** — Detect object boundaries
5️⃣ **Localization** — Draw bounding boxes around detected regions

➡️ Result: Fast and reliable detection of colored objects in real time.

---

## 🚀 Key Features

✅ Multi-color detection (Red, Green, Blue)
✅ Robust to illumination changes (HSV space)
✅ Interactive Gradio dashboard
✅ Works locally or in cloud environments
✅ Minimal hardware requirements

---

## 🛠️ Technical Workflow

### 🌈 HSV Color Segmentation

HSV separates chromatic content from brightness, making detection more stable than RGB under varying lighting conditions.

---

### 🎭 Mask Generation

Each target color uses predefined threshold ranges:

* Lower bound → Minimum hue/saturation/value
* Upper bound → Maximum hue/saturation/value

Pixels within the range are retained; others are suppressed.

---

### 🔍 Contour Detection

Using OpenCV:

* Detect external contours
* Filter noise via area thresholds
* Extract bounding regions

---

### 📦 Spatial Localization

Bounding rectangles are drawn around detected objects to indicate position and extent.

---

## 📂 Project Structure

```text
color-detection-engine/
│
├── app.py                 # Production Gradio application
├── color_detection.ipynb  # Development & experimentation notebook
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

---

## ⚡ Installation & Setup

### 🔹 Local Deployment

```bash
# Clone repository
git clone https://github.com/Tanmay1112004/color-object-detection-opencv.git
cd color-object-detection-opencv

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Access the interface via browser once launched.

---

### ☁️ Cloud Deployment (Google Colab)

Run instantly without local setup:

👉 Open the Colab notebook
👉 Enable GPU (optional)
👉 Execute all cells

Perfect for demos and sharing.

---

## 📊 Detection Capabilities

| Color | Detection Method | Visual Output   |
| ----- | ---------------- | --------------- |
| Red   | HSV Masking      | 🟥 Bounding Box |
| Green | HSV Masking      | 🟩 Bounding Box |
| Blue  | HSV Masking      | 🟦 Bounding Box |

---

## 🧪 Performance Notes

✔ Optimized for indoor lighting conditions
✔ Works in real time on standard CPUs
✔ GPU not required
✔ Accuracy depends on lighting and color purity

---

## 🎯 Practical Applications

This system can serve as a foundation for:

🤖 Robotics object tracking
🏭 Industrial quality control
🚗 Autonomous systems prototyping
📦 Inventory detection
🕶️ Augmented reality interactions
🎮 Gesture-based interfaces

---

## 💼 Recruiter Relevance

Demonstrates essential Computer Vision skills:

🔥 Classical CV techniques (no deep learning required)
🔥 Real-time image processing
🔥 Algorithmic pipeline design
🔥 UI integration for ML applications
🔥 Deployment-ready implementation

➡️ Shows strong fundamentals — highly valued in CV roles.

---

## 🔮 Future Improvements

Potential extensions:

🔹 Support for custom color selection (HEX/RGB picker)
🔹 Multi-object tracking
🔹 Shape + color hybrid detection
🔹 Low-light optimization
🔹 Mobile/web deployment
🔹 Integration with robotics platforms

---

## 🤝 Contributing

Contributions are welcome.

Areas of interest:

✔ Low-light robustness
✔ Noise filtering improvements
✔ Custom color input support
✔ Performance optimization

---

## 📜 License

Released under the MIT License.

---

## 👨‍💻 Author

**Tanmay Kshirsagar**

💻 GitHub: [https://github.com/Tanmay1112004](https://github.com/Tanmay1112004)
🔗 LinkedIn: [https://linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---
