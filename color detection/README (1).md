# 🎨 Color Detection Engine: OpenCV & Gradio Integration

A computer vision application designed to perform real-time color segmentation and object localization. This project demonstrates the implementation of **HSV color-space thresholding** to identify and bound specific chrominance values (Red, Green, Blue) with a streamlined web interface.

---

## 🚀 Key Features

* **Multi-Channel Segmentation:** Dedicated logic for Red, Green, and Blue color masks.
* **Robust Preprocessing:** Utilizes HSV (Hue, Saturation, Value) conversion for improved lighting invariance compared to standard RGB.
* **Web-First Interface:** Built with Gradio for seamless deployment on local machines or cloud environments like Google Colab.
* **Dual-Input Support:** Supports both static image uploads and real-time webcam captures.

---

## 🛠️ Technical Workflow

The system processes imagery through a classic Computer Vision pipeline:

1. **Color Space Conversion:** Standard BGR frames are converted to HSV.
2. **Masking:** Application of range-based thresholding using predefined NumPy arrays.
3. **Contour Detection:** Leveraging `cv2.findContours` to identify external boundaries of the masked objects.
4. **Spatial Localization:** Calculation of bounding boxes to enclose detected regions.

---

## 📂 Project Structure

```text
├── app.py                 # Production Gradio application script
├── color_detection.ipynb  # Interactive development & testing notebook
├── requirements.txt       # Environment dependencies
└── README.md              # Technical documentation

```

---

## ⚡ Installation & Setup

### Local Environment

```bash
# Clone the repository
git clone https://github.com/Tanmay1112004/color-object-detection-opencv.git
cd color-object-detection-opencv

# Install required dependencies
pip install -r requirements.txt

# Launch the application
python app.py

```

### Cloud Environment

For an immediate, zero-config trial, run the project on Google Colab:
[](https://www.google.com/search?q=https://colab.research.google.com/drive/1KFRnfYsEBue_ctgL_qKG6F6GhctXA8UX)

---

## 📊 Performance & Examples

The model is tuned to identify primary colors under standard indoor lighting conditions:

| Target | Logic | Visual Indicator |
| --- | --- | --- |
| **Red** | Masking  | 🟥 Bounding Box |
| **Green** | Masking  | 🟩 Bounding Box |
| **Blue** | Masking  | 🟦 Bounding Box |

---

## 🤝 Contributing

Contributions are encouraged. Please follow the standard fork-and-pull-request workflow. Areas of interest:

* Optimization for low-light environments.
* Support for custom HEX/RGB color inputs.

---

## 📜 License

This project is distributed under the **MIT License**. See `LICENSE` for more information.

---

### 👨‍💻 Developed by

**Tanmay Kshirsagar** [GitHub](https://github.com/Tanmay1112004) | [LinkedIn](https://linkedin.com/in/your-profile)

---
