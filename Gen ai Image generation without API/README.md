# 🎨 CLIP + VQGAN: Open-Source Text-to-Image Synthesis

Transform descriptive text into stunning visual art. This repository leverages **CLIP’s** semantic alignment and **VQGAN’s** high-fidelity image synthesis to provide a fully local, open-source alternative to proprietary AI generators.

---

## 🚀 Key Features

* **Zero-SaaS Dependency:** No API keys, no monthly credits, no vendor lock-in.
* **Hybrid Architecture:** Combines OpenAI’s CLIP for text understanding with Taming Transformers (VQGAN) for generative output.
* **Interactive UI:** Built-in Streamlit dashboard for real-time prompt engineering.
* **Colab Ready:** One-click deployment for users without local GPU resources.

---

## 🛠️ Tech Stack

| Component | Technology | Role |
| --- | --- | --- |
| **Language** | Python 3.8+ | Core Logic |
| **Deep Learning** | PyTorch | Model Backend |
| **Vision/Text** | CLIP + VQGAN | Generative Backbone |
| **Deployment** | Streamlit | Web Interface |
| **Platform** | Google Colab | Cloud Acceleration |

---

## 📦 Installation & Setup

### 1. Environment Configuration

```bash
git clone https://github.com/your-username/clip-vqgan-text2image.git
cd clip-vqgan-text2image
pip install -r requirements.txt

```

### 2. Model Weight Management

You must download the pre-trained ImageNet weights. Use the links below and organize your `models` directory as follows:

* 📥 [VQGAN Checkpoint (.ckpt)](https://heibox.uni-heidelberg.de/f/867b05fc8c4841768640/?dl=1)
* 📥 [VQGAN Config (.yaml)](https://heibox.uni-heidelberg.de/f/274fb24ed38341bfa753/?dl=1)

**Required Directory Structure:**

```text
.
└── models/
    └── vqgan_imagenet_f16_16384/
        ├── checkpoints/
        │   └── last.ckpt
        └── configs/
            └── model.yaml

```

---

## ▶️ How to Use

### Local Dashboard (Streamlit)

Ideal for local machines with NVIDIA GPUs.

```bash
streamlit run app.py

```

*Enter your prompt in the sidebar and watch the iterative generation process in real-time.*

### Cloud Notebook (Google Colab)

No local GPU? No problem.

1. Open `GenerativeAI_Colab.ipynb`.
2. Select **Runtime > Change runtime type > GPU**.
3. Run the cells to launch the generation interface.

---

## 📋 Hardware Requirements

* **Minimum:** 8GB RAM + Quad-core CPU (Slow).
* **Recommended:** NVIDIA GPU (8GB+ VRAM) with CUDA support.
* **OS:** Linux, Windows (WSL2), or macOS (M-series support via MPS varies).

---

## 📄 License & Attribution

Distributed under the **MIT License**. See `LICENSE` for more information.

*This project builds upon the foundational research of OpenAI (CLIP) and the Taming Transformers team.*

---

## ⭐ Support the Project

If this repository helped you explore the world of Generative AI, please **give it a star!** It helps others find this resource.

**Author:** Tanmay Kshirsagar

**Contact:** [Email](mailto:tanmaykshirsagar001@gmail.com) | [GitHub](https://www.google.com/search?q=https://github.com/your-username)

---
