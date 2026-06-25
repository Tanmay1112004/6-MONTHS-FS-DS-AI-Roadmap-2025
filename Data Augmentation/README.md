---

# ✨ Image Data Augmentation Playground

An **interactive, Gradio-powered web application** for visualizing and experimenting with **image data augmentation techniques** in real time.

This tool allows you to upload an image, fine-tune augmentation parameters (rotation, zoom, shifts, shear, flips, and fill modes), and instantly preview multiple augmented samples.
Built using **TensorFlow / Keras** for augmentation logic and **Gradio** for a clean, intuitive UI.

---

## 🖼️ Demo Preview

<p align="center">
  <img src="https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Data%20Augmentation/screenshots/Screenshot%202025-09-02%20083142.png" width="45%" />
  <img src="https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Data%20Augmentation/screenshots/Screenshot%202025-09-02%20083422.png" width="45%" />
</p>

<p align="center">
  <img src="https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Data%20Augmentation/screenshots/Screenshot%202025-09-02%20083557.png" width="45%" />
  <img src="https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Data%20Augmentation/screenshots/Screenshot%202025-09-02%20083641.png" width="45%" />
</p>

---

## 🚀 Key Features

* 📂 Upload images in **JPG / PNG** format
* 🎛️ Fully customizable augmentation controls:

  * Rotation range
  * Width & height shifts
  * Shear and zoom transformations
  * Horizontal flip toggle
  * Multiple fill modes (`nearest`, `reflect`, `wrap`, `constant`)
* 🖼️ Real-time preview with gallery output
* ⚡ Generate **multiple augmented samples** in one click
* 🌐 Works seamlessly **locally** and in **Google Colab**

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/Tanmay1112004/image-data-augmentation-gradio.git
cd image-data-augmentation-gradio
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

### Local Execution

```bash
python app.py
```

### Google Colab

```python
!pip install gradio tensorflow --quiet
```

```python
import gradio as gr
import tensorflow as tf
```

Paste the contents of `app.py`, run the cell, and launch the app 🚀.

---

## 📂 Project Structure

```
image-data-augmentation-gradio/
│── app.py                # Main Gradio application
│── requirements.txt      # Project dependencies
│── README.md             # Documentation
│── demo/                 # Screenshots / demo assets
```

---

## ✅ Requirements

* Python **3.8+**
* TensorFlow **2.x**
* Gradio **4.x**
* NumPy
* Pillow

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository, improve the UI/UX, add new augmentation techniques, or optimize performance.

If this project helped you, ⭐ the repo — it genuinely helps.

---

