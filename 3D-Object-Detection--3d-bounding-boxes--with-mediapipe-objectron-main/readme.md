# 📦 Objectron Streamlit App (MediaPipe)

A production-ready **3D Object Detection Web App** built using **MediaPipe Objectron** and **Streamlit**.

This application detects **3D bounding boxes** around real-world objects and visualizes:

* 3D landmarks
* Rotation matrices
* Translation vectors
* Pose data export (CSV)

Designed to run seamlessly in **GitHub Codespaces (Python 3.11)** or locally.

Clean UI. Practical 3D vision. Interview-ready execution.

---

## 📸 Demo Preview

![Image](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/3D-Object-Detection--3d-bounding-boxes--with-mediapipe-objectron-main/screenshots/Screenshot%202025-09-07%20184454.png)

![Image](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/3D-Object-Detection--3d-bounding-boxes--with-mediapipe-objectron-main/screenshots/Screenshot%202025-09-07%20185120.png)

![Image]()

![Image]()

---

## 📌 Project Overview

This project demonstrates applied **3D computer vision** using MediaPipe’s Objectron pipeline.

It performs:

* Object detection
* 3D bounding box estimation
* Pose estimation (6DoF)
* Structured data export

It bridges deep learning inference with interactive UI deployment.

---

## 🚀 Key Features

* 🖼️ Image input via **URL** or **file upload**
* 🪑 Object model selection:

  * Cup
  * Chair
  * Shoe
  * Camera
* 🎨 Colored 3D landmarks (clear visibility on all backgrounds)
* 📊 Pose output:

  * Rotation Matrix (3×3)
  * Translation Vector (3D position)
* 📥 CSV export of pose data
* ⚡ Optional auto-resize for faster inference

---

## 🧠 Technical Highlights

* 3D bounding box regression
* 6DoF pose estimation
* Landmark projection visualization
* Streamlit UI integration
* CSV generation from inference results
* Devcontainer-based cloud development setup

This project demonstrates understanding beyond 2D detection — entering real-world 3D spatial reasoning.

---

## 🛠 Tech Stack

| Layer               | Technology          |
| ------------------- | ------------------- |
| 3D Vision Framework | MediaPipe Objectron |
| Web UI              | Streamlit           |
| Environment         | GitHub Codespaces   |
| Language            | Python 3.11         |
| Data Export         | CSV                 |

---

## ⚡ Quick Start (GitHub Codespaces – Recommended)

1️⃣ Fork or clone the repository
2️⃣ Go to **Code → Codespaces → Create Codespace**
3️⃣ Wait for the `.devcontainer` build
4️⃣ Run:

```bash
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0 --server.enableCORS false
```

5️⃣ Open forwarded port **8501**

App launches instantly in browser.

---

## 🖥️ Local Setup (Optional)

### 1️⃣ Install Python 3.11

### 2️⃣ Clone Repository

```bash
git clone 
cd <repo>
```

### 3️⃣ Create Virtual Environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run App

```bash
streamlit run streamlit_app.py
```

---

## 📂 Repository Structure

```
repo-root/
│
├── .devcontainer/           # Codespaces container config
│   ├── Dockerfile
│   └── devcontainer.json
│
├── streamlit_app.py         # Main app logic
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

Organized for cloud-first reproducibility.

---

## 📊 Pose Output Explanation

### Rotation Matrix (3×3)

Represents object orientation in 3D space.

### Translation Vector (x, y, z)

Represents object position relative to camera.

This data enables:

* AR applications
* Robotics grasp planning
* Spatial analytics
* 3D scene understanding

---

## 🐞 Troubleshooting

### `ImportError: libGL.so.1`

Run:

```bash
sudo apt-get update && sudo apt-get install -y libgl1 libglib2.0-0
```

Or rebuild the Codespace container.

---

### Slow Performance on Large Images

Enable **Auto-resize** in the app
Recommended `max_dim = 800–1200`

---

## 🎯 What This Project Demonstrates

* Advanced computer vision knowledge
* 3D spatial transformations
* Pose estimation understanding
* ML-to-UI deployment skills
* Cloud-based development workflow

This is a strong portfolio project for:

* Computer Vision roles
* Robotics applications
* AR/VR systems
* Applied AI Engineering

---

## 🔮 Future Enhancements

* Real-time webcam 3D detection
* Depth estimation integration
* Multi-object simultaneous tracking
* WebGL 3D rendering
* Deployment on cloud (Render / AWS / GCP)

---

## 📄 License

MIT License

---

### 👨‍💻 Author

**Tanmay**

Open to opportunities in:

* Computer Vision
* 3D Vision Systems
* AI/ML Engineering
* Applied Deep Learning

---
