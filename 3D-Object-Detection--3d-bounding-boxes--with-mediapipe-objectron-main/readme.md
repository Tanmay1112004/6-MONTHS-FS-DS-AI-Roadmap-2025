# 📦 Objectron Streamlit App (MediaPipe)

A **Streamlit web app** that uses **MediaPipe Objectron** to detect 3D bounding boxes around objects (cup, chair, shoe, camera) in images.
It displays **colored 3D landmarks**, **rotation matrices**, **translation vectors**, and lets you **download pose data as CSV**.

Runs inside **GitHub Codespaces (Python 3.11)** or locally.
---
## Demo Images 
![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/3D-Object-Detection--3d-bounding-boxes--with-mediapipe-objectron-main/screenshots/Screenshot%202025-09-07%20184454.png)
![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/3D-Object-Detection--3d-bounding-boxes--with-mediapipe-objectron-main/screenshots/Screenshot%202025-09-07%20185120.png)
![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/3D-Object-Detection--3d-bounding-boxes--with-mediapipe-objectron-main/screenshots/Screenshot%202025-09-07%20185135.png)
![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/3D-Object-Detection--3d-bounding-boxes--with-mediapipe-objectron-main/screenshots/Screenshot%202025-09-07%20185227.png)

---

## 🚀 Features

* 🖼️ Input image via **URL** or **file upload**
* 🪑 Choose object model: **Cup / Chair / Shoe / Camera**
* 🎨 Colored 3D bounding boxes & landmarks (visible even on white backgrounds)
* 📊 Rotation matrix & translation vector tables
* 📥 Download pose data as **CSV**
* ⚡ Optional auto-resize for large images (faster inference)

---

## ⚡ Quick Start (GitHub Codespaces)

1. Fork or clone this repo to your GitHub.
2. In your repo → **Code → Codespaces → Create Codespace** (choose branch).
3. Wait for the devcontainer to build (first time takes a few mins).
4. In the Codespace terminal, run:

   ```bash
   streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0 --server.enableCORS false
   ```
5. Open the forwarded port **8501** → app loads in browser.

---

## 🖥️ Local Run (optional)

1. Install **Python 3.11** on your system.
2. Clone repo and create venv:

   ```bash
   git clone <your-repo-url>
   cd <repo>
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:

   ```bash
   streamlit run streamlit_app.py
   ```

---

## 🛠️ Repo Structure

```
📂 repo-root
 ┣ 📂 .devcontainer       # Devcontainer setup for GitHub Codespaces
 ┃ ┣ 📜 Dockerfile
 ┃ ┗ 📜 devcontainer.json
 ┣ 📜 streamlit_app.py    # Main Streamlit app
 ┣ 📜 requirements.txt    # Python dependencies
 ┗ 📜 README.md           # This file
```

---

## 🐞 Troubleshooting

* **Error: `ImportError: libGL.so.1`**
  → The Codespace Dockerfile already installs `libgl1`. If you created Codespace before adding `.devcontainer`, rebuild it or run:

  ```bash
  sudo apt-get update && sudo apt-get install -y libgl1 libglib2.0-0
  ```

* **Mediapipe install issues**
  → Rebuild the Codespace so dependencies are installed inside the container.

* **App slow on big images**
  → Enable **Auto-resize** in app (recommended `max_dim=800–1200`).

---

## 📄 License

MIT License — feel free to modify and use.

---
