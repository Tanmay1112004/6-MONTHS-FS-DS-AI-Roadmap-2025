# 🧠 Face & Hand Landmarks Detection

### Mediapipe • OpenCV • Streamlit

> Real-time **Face & Hand Landmark Detection** using Google **Mediapipe**, powered by **OpenCV** and wrapped in an interactive **Streamlit** web app.
> Clean UI. Fast inference. Beginner-friendly setup.

---

## 🚀 Features

* 🔍 **Real-time Face & Hand Landmark Detection**
* 📷 Supports **Laptop Webcam** & **Browser Webcam (Snapshot Mode)**
* ⚡ Fast & lightweight using Mediapipe
* 🌐 Interactive **Streamlit Web App**
* 🧪 Works locally & on **GitHub Codespaces**
* 🧩 Clean modular Python code (easy to extend)

---

## 🛠 Tech Stack

| Tool                  | Purpose                        |
| --------------------- | ------------------------------ |
| **Python**            | Core programming language      |
| **Mediapipe**         | Face & hand landmark detection |
| **OpenCV**            | Image & video processing       |
| **Streamlit**         | Web UI                         |
| **GitHub Codespaces** | Cloud-based dev environment    |

---

## 🐍 Supported Python Versions

> ⚠️ **Important**

* ✅ **Python 3.10 or 3.11 only**
* ❌ Python 3.12+ is **not supported** (Mediapipe wheels break)

---

## 📸 Demo Screenshots

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Face-and-Hand-Landmarks-Detection-using-Python---Mediapipe--OpenCV/snapshots/snap_20250909_043639.png)
![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Face-and-Hand-Landmarks-Detection-using-Python---Mediapipe--OpenCV/snapshots/snap_20250909_043727.png)
![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Face-and-Hand-Landmarks-Detection-using-Python---Mediapipe--OpenCV/snapshots/snap_20250909_043929.png)
![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Face-and-Hand-Landmarks-Detection-using-Python---Mediapipe--OpenCV/snapshots/snap_20250909_044150.png)

---

## ⚡ Quick Start — Local (Ubuntu / WSL Recommended)

### 1️⃣ Install System Dependencies

(Fixes `libGL.so.1` error)

```bash
sudo apt update
sudo apt install -y libgl1 libglib2.0-0 ffmpeg
```

---

### 2️⃣ Create Virtual Environment (Python 3.11)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 3️⃣ Run the App

```bash
streamlit run app.py
```

👉 Open in browser: **[http://localhost:8501](http://localhost:8501)**

---

## ☁️ Quick Start — GitHub Codespaces

Perfect if you don’t want local setup headaches.

### Steps:

1. Push this repo to GitHub
2. Open repo → **Code → Open with Codespaces → New Codespace**
3. Codespace auto-builds using `.devcontainer`
   (Python 3.11 + system libraries preinstalled)
4. Run inside Codespaces terminal:

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

5. Open the **forwarded port 8501** from the Ports tab

---

### 📌 Codespaces Camera Note (Important)

🚫 Codespaces **cannot access your laptop webcam directly**.

✅ Use **Browser Webcam (Snapshot Mode)**
This captures frames from your browser camera and sends them to the app — smooth and reliable.

---

## 🧯 Troubleshooting

### ❌ `ImportError: libGL.so.1`

✔ Fix:

```bash
sudo apt install -y libgl1
```

or use `opencv-python-headless` (already included in requirements).

---

### ❌ Mediapipe Installation Errors

✔ Fix:

* Use **Python 3.10 or 3.11**
* Avoid Python 3.12+

---

### ❌ Webcam Not Working in Codespaces

✔ Fix:

* Use **Browser Webcam (Snapshot Mode)**
* Or run locally for direct webcam access

---

## 📜 Step-by-Step (Copy–Paste Friendly)

### 🔹 Local Setup (Ubuntu / WSL)

```bash
# Clone repository
git clone https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/edit/main/Face-and-Hand-Landmarks-Detection-using-Python---Mediapipe--OpenCV
cd face-hand-landmarks

# Install system dependencies
sudo apt update
sudo apt install -y libgl1 libglib2.0-0 ffmpeg

# Setup virtual environment
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Run application
streamlit run app.py
```

Open 👉 **[http://localhost:8501](http://localhost:8501)**

---

### 🔹 GitHub Codespaces

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

Open forwarded port **8501**.

---

## 💡 Pro Tips

* For **real-time server webcam**, run locally
* For **zero-setup demo**, use Codespaces + browser webcam
* Want to extend?

  * Add gesture recognition ✋
  * Add face mesh analytics 🧠
  * Export landmarks to CSV 📊

---

## ⭐ If You Like This Project

* Give it a ⭐ on GitHub
* Fork it
* Build something cooler on top of it

**Ship fast. Learn faster. 🚀**

---
