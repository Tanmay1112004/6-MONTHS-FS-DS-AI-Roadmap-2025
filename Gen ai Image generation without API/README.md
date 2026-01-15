# 🎨 CLIP + VQGAN Text-to-Image Generator

Create **high-quality, AI-generated images** from natural language prompts using **CLIP** and **VQGAN (Taming Transformers)** — **no API keys, no paid services**, just pure open-source power.

This project combines the semantic understanding of **CLIP** with the generative strength of **VQGAN** to transform text into visually compelling artwork.

---

## 🚀 Key Highlights

* 🧠 **Text-to-Image Generation** using CLIP + VQGAN
* ⚡ Powered by **pre-trained open-source models**
* 🖥️ **Streamlit UI** for interactive prompt-based generation
* ☁️ **Google Colab ready** with GPU acceleration
* 🔓 No API keys or external services required

---

## 🛠️ Tech Stack

* **Python**
* **PyTorch**
* **CLIP**
* **VQGAN (Taming Transformers)**
* **Streamlit**
* **Google Colab**

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/clip-vqgan-text2image.git
cd clip-vqgan-text2image
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Download Model Files

Download the following pre-trained VQGAN files:

* 📥 [VQGAN Checkpoint](https://heibox.uni-heidelberg.de/f/867b05fc8c4841768640/?dl=1)
* 📥 [VQGAN Config](https://heibox.uni-heidelberg.de/f/274fb24ed38341bfa753/?dl=1)

Place them in the directory structure below:

```
models/
└── vqgan_imagenet_f16_16384/
    ├── checkpoints/
    │   └── last.ckpt
    └── configs/
        └── model.yaml
```

---

## ▶️ Usage

### 🔹 Run with Streamlit (Local)

```bash
streamlit run app.py
```

* Open the generated local URL
* Enter a text prompt
* Watch the model generate images in real time 🎨

---

### 🔹 Run on Google Colab

1. Open `GenerativeAI_Colab.ipynb`
2. Enable **GPU runtime**
3. Run all cells
4. Input your text prompt and generate images

Perfect for experimentation without local setup.

---

## 📋 System Requirements

* Python **3.8+**
* PyTorch **1.10+**
* CUDA-enabled GPU (strongly recommended for faster generation)

---

## 📄 License

This project is licensed under the **MIT License**.
Free to use, modify, and distribute.

---

## ⭐ Final Note

If you’re into **Generative AI, Computer Vision, or creative ML**, this project is a solid hands-on playground.
Fork it. Break it. Improve it. Ship it.

**If this helped you, don’t forget to star the repo ⭐**
That’s the open-source handshake 🤝
