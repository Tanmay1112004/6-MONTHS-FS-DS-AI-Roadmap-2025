# CLIP + VQGAN Text-to-Image Generator 🎨

Generate stunning images from text prompts using **CLIP** and **VQGAN/Taming Transformers** – no API keys required!

## 🔹 Features
- Text-to-image generation
- Uses pre-trained CLIP + VQGAN models
- Streamlit frontend for easy interaction
- Runs on Google Colab with GPU support

## 🔹 Installation
Clone the repo:

```bash
git clone https://github.com/your-username/clip-vqgan-text2image.git
cd clip-vqgan-text2image
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Download model checkpoints & configs:

* [VQGAN checkpoint](https://heibox.uni-heidelberg.de/f/867b05fc8c4841768640/?dl=1)
* [VQGAN config](https://heibox.uni-heidelberg.de/f/274fb24ed38341bfa753/?dl=1)

Place them in:

```
./models/vqgan_imagenet_f16_16384/checkpoints/last.ckpt
./models/vqgan_imagenet_f16_16384/configs/model.yaml
```

## 🔹 Usage

### Using Streamlit

```bash
streamlit run app.py
```

Open the provided URL and enter your text prompt to generate images.

### Using Colab

* Open `GenerativeAI_Colab.ipynb`
* Run all cells
* Enter your prompts and view generated images

## 🔹 Requirements

* Python 3.8+
* PyTorch 1.10+
* CUDA-enabled GPU recommended

## 🔹 Screenshots

*(Add some generated images here)*

## 🔹 License

MIT License

```
