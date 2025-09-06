# 🚗 Object Tracking Streamlit App

An interactive app for object detection + tracking using OpenCV & Streamlit.

## ✨ Features
- Upload videos (`.mp4`, `.avi`, `.mov`)
- Adjust tracking settings:
  - Frame skip (speed)
  - Resize width
  - Minimum object area
- Progress bar while processing
- Summary metrics after run
- Download processed video

## ⚡ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py


App will open at http://localhost:8501
.

🐳 Run in GitHub Codespaces
sudo apt-get update && sudo apt-get install -y libgl1
pip install -r requirements.txt
streamlit run app.py --server.port 8000 --server.address 0.0.0.0


Then open forwarded port in your browser.


---

⚡ This new version is **much faster** because:  
- Skips live frame rendering (`st.image`) → only shows final processed video.  
- Lets you resize + skip frames = control performance.  
- Adds stats, metrics, and a clean UI.  

---
