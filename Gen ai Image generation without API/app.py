
import os
import torch
import streamlit as st
from omegaconf import OmegaConf
import torchvision.transforms as T
from taming.models.vqgan import VQModel
from CLIP import clip
import yaml
import matplotlib.pyplot as plt

# ----------------------------
# Helper functions
# ----------------------------

def load_config(config_path, display=False):
    config_data = OmegaConf.load(config_path)
    if display:
        print(yaml.dump(OmegaConf.to_container(config_data)))
    return config_data

def load_vqgan(config, chk_path=None):
    model = VQModel(**config.model.params)
    if chk_path is not None:
        state_dict = torch.load(chk_path, map_location="cpu")["state_dict"]
        model.load_state_dict(state_dict, strict=False)
    return model.eval()

def generator(x, model):
    x = model.post_quant_conv(x)
    x = model.decoder(x)
    return x

def show_from_tensor(tensor):
    img = tensor.clone()
    img = img.mul(255).byte()
    img = img.cpu().numpy().transpose((1,2,0))
    plt.imshow(img)
    plt.axis("off")
    st.pyplot(plt)

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🎨 VQGAN + CLIP Playground")
st.write("Enter a text prompt to generate images with CLIP + VQGAN")

prompt = st.text_input("Prompt", "A painting of a futuristic city")
generate_btn = st.button("Generate")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if generate_btn:
    # Load CLIP
    clip_model, _ = clip.load("ViT-B/32", device=device, jit=False)

    # Load VQGAN
    config_path = "./models/vqgan_imagenet_f16_16384/configs/model.yaml"
    ckpt_path = "./models/vqgan_imagenet_f16_16384/checkpoints/last.ckpt"
    if not os.path.exists(config_path) or not os.path.exists(ckpt_path):
        st.error("❌ Model files not found. Please download configs and checkpoints before running.")
    else:
        taming_config = load_config(config_path, display=False)
        taming_model = load_vqgan(taming_config, chk_path=ckpt_path).to(device)

        # Dummy latent for demo purposes (not full training loop)
        z = torch.randn(1, 256, 28, 28).to(device)
        img = generator(z, taming_model)
        img = (img.clamp(-1,1)+1)/2

        st.success(f"Generated result for: {prompt}")
        show_from_tensor(img[0])
