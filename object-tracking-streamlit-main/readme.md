# 🚗 Object Tracking Streamlit App

A high-performance **object detection and tracking web app** built using **OpenCV** and **Streamlit**.
Designed for speed, clarity, and hands-on experimentation with video analytics.

---
## Demo images 

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/object-tracking-streamlit-main/screenshots/Screenshot%202025-09-06%20130009.png)                                                                                                                                                  ![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/object-tracking-streamlit-main/screenshots/Screenshot%202025-09-06%20130235.png)                                                                                                                                                  ![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/object-tracking-streamlit-main/screenshots/Screenshot%202025-09-06%20130304.png)                                                                                                                                                  ![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/object-tracking-streamlit-main/screenshots/Screenshot%202025-09-06%20130331.png)
---

## 🔍 Overview

This app allows you to upload a video, apply object tracking with customizable parameters, and download the processed output — all through an intuitive web interface.

Built for:

* Computer Vision learners
* Data Science / AI projects
* Quick demos and experimentation

---

## ✨ Key Features

* 📤 Upload video files (`.mp4`, `.avi`, `.mov`)
* 🎛️ Adjustable tracking controls:

  * **Frame Skip** – optimize speed vs accuracy
  * **Resize Width** – control resolution & performance
  * **Minimum Object Area** – filter noise
* 📊 Real-time progress bar during processing
* 📈 Post-processing summary metrics
* 📥 Download the final processed video
* 🧼 Clean, minimal, and responsive UI

---

## 🚀 Performance Optimized

This version is **significantly faster** due to:

* 🚫 No live frame rendering (`st.image` removed)
* ⚡ Frame skipping for faster processing
* 📐 Dynamic resizing to reduce computation
* 🧠 Smarter tracking thresholds

Result: **Faster execution, lower memory usage, better UX.**

---

## ⚙️ Run Locally

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start the App

```bash
streamlit run app.py
```

### 3️⃣ Open in Browser

```text
http://localhost:8501
```

---

## 🐳 Run in GitHub Codespaces

### 1️⃣ Install System Dependency

```bash
sudo apt-get update && sudo apt-get install -y libgl1
```

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit

```bash
streamlit run app.py --server.port 8000 --server.address 0.0.0.0
```

### 4️⃣ Access the App

Open the **forwarded port (8000)** in your browser.

---

## 🧠 Tech Stack

* **Python**
* **OpenCV**
* **Streamlit**
* **NumPy**

---

## 📌 Use Cases

* Object tracking demos
* Computer vision coursework
* Rapid prototyping
* Portfolio projects
* Interview discussions (CV + performance tuning)

---

## 🤝 Contributions

Pull requests are welcome.
If you have ideas for new trackers, metrics, or UI improvements — let’s ship it.

---

🔥 **Fast. Clean. Practical.**
This app keeps things simple while delivering real value.
