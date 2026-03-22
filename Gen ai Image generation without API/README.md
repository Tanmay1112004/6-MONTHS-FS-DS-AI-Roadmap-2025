# 🎨 CLIP + VQGAN — Open-Source Text-to-Image Generator

Generate striking visual artwork directly from natural language prompts using a fully local, open-source pipeline.

This project combines **CLIP’s semantic understanding** with **VQGAN’s high-fidelity image synthesis** to deliver a powerful alternative to proprietary AI image generators — with **zero API dependency**.

---

## ✨ Project Highlights

🧠 Prompt-to-image generation using state-of-the-art research models
🔐 Fully local execution — no cloud lock-in
🎛️ Interactive dashboard for prompt engineering
⚡ GPU-accelerated generation pipeline
☁️ Google Colab support for non-GPU users

---

## 🧠 How It Works

1. **Text Prompt → CLIP Encoding**
   CLIP converts the input text into semantic embeddings.

2. **Latent Optimization → VQGAN**
   VQGAN iteratively generates images that best match CLIP’s understanding.

3. **Feedback Loop**
   CLIP scores each generated image and guides refinement.

➡️ Result: Images that align closely with the textual description.

---

## 🚀 Key Features

✅ No API keys or subscription required
✅ Fully open-source generative pipeline
✅ High-resolution artistic outputs
✅ Real-time visual feedback during generation
✅ Flexible prompt experimentation

---

## 🛠️ Technology Stack

| Layer           | Technology                  | Purpose               |
| --------------- | --------------------------- | --------------------- |
| Language        | Python 3.8+                 | Core implementation   |
| Deep Learning   | PyTorch                     | Model execution       |
| Vision-Language | CLIP                        | Text understanding    |
| Image Generator | VQGAN (Taming Transformers) | Image synthesis       |
| Interface       | Streamlit                   | Interactive dashboard |
| Cloud Option    | Google Colab                | GPU acceleration      |

---

## 📦 Installation & Setup

### 🔹 Clone Repository

```bash id="6hndt7"
git clone https://github.com/your-username/clip-vqgan-text2image.git
cd clip-vqgan-text2image
```

---

### 🔹 Install Dependencies

```bash id="9psh1y"
pip install -r requirements.txt
```

---

## 📥 Model Weights Setup

Download pre-trained VQGAN ImageNet weights:

* 📥 VQGAN Checkpoint (.ckpt)
* 📥 VQGAN Config (.yaml)

Place them in the following structure:

```text
models/
└── vqgan_imagenet_f16_16384/
    ├── checkpoints/
    │   └── last.ckpt
    └── configs/
        └── model.yaml
```

---

## ▶️ Usage

### 🖥️ Local Dashboard (Streamlit)

Best for systems with NVIDIA GPU support.

```bash id="2q3ibq"
streamlit run app.py
```

Enter a text prompt and observe the iterative image generation process in real time.

---

### ☁️ Google Colab Deployment

Ideal for users without local GPU access.

1. Open `GenerativeAI_Colab.ipynb`
2. Enable GPU runtime
3. Run all cells

---

## 📊 Hardware Requirements

| Tier         | Specification                                    | Performance |
| ------------ | ------------------------------------------------ | ----------- |
| Minimum      | 8GB RAM + CPU                                    | Very slow   |
| Recommended  | NVIDIA GPU (8GB+ VRAM)                           | Optimal     |
| Supported OS | Linux, Windows (WSL2), macOS (M-series via MPS*) |             |

* Performance on Apple Silicon may vary.

---

## 🎯 What This Project Demonstrates

### 🧠 Generative AI Skills

✔ Vision-language model integration
✔ Latent-space optimization techniques
✔ Prompt-driven generation workflows
✔ Research-to-application implementation

---

### 🏗️ Engineering Skills

✔ End-to-end AI pipeline design
✔ Local deployment of heavy ML models
✔ Interactive UI development
✔ GPU-accelerated computing

---

## 💼 Recruiter Relevance

This project showcases real capabilities needed for modern AI roles:

🔥 Building generative AI systems from research papers
🔥 Integrating multimodal models
🔥 Deploying compute-intensive ML applications
🔥 Working with open-source AI stacks

➡️ Demonstrates both theoretical understanding and practical implementation.

---

## 🔮 Possible Extensions

Future enhancements could include:

🔹 Stable Diffusion integration
🔹 Batch generation mode
🔹 Style transfer presets
🔹 Prompt templates library
🔹 Web deployment (Hugging Face Spaces / AWS)
🔹 Fine-tuned domain-specific models

---

## 📄 License & Attribution

Released under the MIT License.

This project builds upon foundational work by:

* OpenAI (CLIP)
* Taming Transformers research team (VQGAN)

---

## ⭐ Support

If this project helped you explore Generative AI, consider giving it a ⭐ on GitHub.

---

## 👤 Author

**Tanmay Kshirsagar**

📧 [tanmaykshirsagar001@gmail.com](mailto:tanmaykshirsagar001@gmail.com)
💻 GitHub: [https://github.com/Tanmay1112004](https://github.com/Tanmay1112004)

---

