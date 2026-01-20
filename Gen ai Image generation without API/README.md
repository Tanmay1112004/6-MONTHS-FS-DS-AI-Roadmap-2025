# 🎨 CLIP + VQGAN Text-to-Image Generator

Generate **stunning, high-quality images from plain English prompts** using the power duo of **CLIP** and **VQGAN (Taming Transformers)**.
No APIs. No paywalls. No vendor lock-in. Just **pure open-source Generative AI**.

This project fuses:

* **CLIP’s semantic understanding** of text
* **VQGAN’s creative image synthesis**

Result? Text → Art. Simple. Powerful. Fun.

---

## 🚀 Key Highlights

* 🧠 **Text-to-Image Generation** with CLIP + VQGAN
* ⚡ Uses **pre-trained open-source models**
* 🖥️ **Streamlit-based UI** for interactive prompt generation
* ☁️ **Google Colab compatible** with GPU acceleration
* 🔓 **No API keys or paid services required**

Old-school research meets modern creativity.

---

## 🛠️ Tech Stack

* **Python**
* **PyTorch**
* **CLIP**
* **VQGAN (Taming Transformers)**
* **Streamlit**
* **Google Colab**

Battle-tested tools. Zero fluff.

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/clip-vqgan-text2image.git
cd clip-vqgan-text2image
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Download Pre-trained VQGAN Models

Download the required VQGAN files:

* 📥 **VQGAN Checkpoint**
  [https://heibox.uni-heidelberg.de/f/867b05fc8c4841768640/?dl=1](https://heibox.uni-heidelberg.de/f/867b05fc8c4841768640/?dl=1)

* 📥 **VQGAN Config**
  [https://heibox.uni-heidelberg.de/f/274fb24ed38341bfa753/?dl=1](https://heibox.uni-heidelberg.de/f/274fb24ed38341bfa753/?dl=1)

Place them in the following directory structure:

```
models/
└── vqgan_imagenet_f16_16384/
    ├── checkpoints/
    │   └── last.ckpt
    └── configs/
        └── model.yaml
```

Structure matters. Models won’t load without it.

---

## ▶️ Usage

### 🔹 Run Locally with Streamlit

```bash
streamlit run app.py
```

* Open the local Streamlit URL
* Enter a text prompt
* Watch the model iteratively generate artwork 🎨

Instant feedback. Creative chaos.

---

### 🔹 Run on Google Colab

1. Open `GenerativeAI_Colab.ipynb`
2. Enable **GPU runtime**
3. Run all cells
4. Enter your text prompt and generate images

Zero setup. Maximum experimentation.

---

## 📋 System Requirements

* **Python 3.8+**
* **PyTorch 1.10+**
* **CUDA-enabled GPU** (strongly recommended for performance)

CPU works. GPU flies.

---

## 📄 License

Licensed under the **MIT License**.
Free to use, modify, and ship. No strings attached.

---

## ⭐ Final Note

If you’re into **Generative AI, Computer Vision, or creative ML**, this project is a hands-on playground worth exploring.

Fork it.
Break it.
Improve it.
Ship it.

And if it helped you — **drop a star ⭐**
That’s the open-source respect signal 🤝
