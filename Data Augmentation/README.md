# ✨ Image Data Augmentation Playground

This project is a **Gradio-powered interactive app** that lets you visualize and experiment with **image data augmentation** in real time.  
Upload an image, tweak augmentation parameters (rotation, zoom, shift, shear, flips, fill modes), and instantly preview augmented samples.  
Built with **TensorFlow/Keras** + **Gradio**.

---

## 🚀 Features
- 📂 Upload any image (JPG/PNG)
- 🎛️ Adjust augmentation parameters:
  - Rotation range
  - Width/Height shift
  - Shear & Zoom
  - Horizontal flip toggle
  - Fill modes (`nearest`, `reflect`, `wrap`, `constant`)
- 🖼️ Live preview with gallery view
- ⚡ Generates multiple augmented samples at once
- 🌐 Runs seamlessly in **Google Colab** or locally

---

## 🛠️ Installation

Clone the repo:
```bash
git clone https://github.com/your-username/image-data-augmentation-gradio.git
cd image-data-augmentation-gradio
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the app:

```bash
python app.py
```

Or directly in **Google Colab**:

```python
!pip install gradio tensorflow --quiet
```

```python
import gradio as gr
import tensorflow as tf
```

Then paste the code from `app.py` and launch 🚀.

---

## 📸 Demo

<img src="demo/demo.png" width="700">

---

## 📂 Project Structure

```
image-data-augmentation-gradio/
│── app.py                # Gradio app code
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── demo/                 # Screenshots / GIFs
```

---

## ✅ Requirements

* Python 3.8+
* TensorFlow 2.x
* Gradio 4.x
* NumPy, Pillow

---

## 🤝 Contributing

PRs and feature requests are welcome! Feel free to fork this repo and enhance the UI/UX or add new augmentation features.

---

## 📜 License

MIT License © 2025

```

---

👉 Do you also want me to write a **`requirements.txt`** for you (so your repo is plug-and-play), or do you prefer keeping dependencies inside Colab only?
```
