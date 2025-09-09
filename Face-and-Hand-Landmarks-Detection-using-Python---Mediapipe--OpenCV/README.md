# Face & Hand Landmarks — Mediapipe + OpenCV + Streamlit

## Supported Python
**Only Python 3.10 or 3.11** (Mediapipe wheels may not support 3.12+).

---

## Quick run — Local (Ubuntu / WSL recommended)
1. Install system libs (fixes `libGL.so.1` error):
   ```bash
   sudo apt update
   sudo apt install -y libgl1 libglib2.0-0 ffmpeg
````

2. Create venv (python3.11):

   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Start app:

   ```bash
   streamlit run app.py
   ```

   Open [http://localhost:8501](http://localhost:8501)

---

## Quick run — GitHub Codespaces

1. Push this repo to GitHub.
2. Open the repo → green **Code** button → **Open with Codespaces** → create new Codespace.
3. Codespace will build using `.devcontainer` (Python 3.11 + system libs installed).
4. In the Codespaces terminal:

   ```bash
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```
5. Use the forwarded port UI in Codespaces to open the app in the browser.

**Note:** Codespaces cannot access your laptop webcam as a server device. Use the **Browser webcam (snapshot)** mode — it captures from your browser camera and sends a snapshot to the app.

---

## Troubleshooting

* `ImportError: libGL.so.1` → install system package `libgl1` (see commands above) OR use `opencv-python-headless` as in requirements.
* `Mediapipe wheel errors on install` → use Python 3.10 or 3.11; avoid 3.12+.
* Webcam not showing in Codespaces → use Browser webcam (snapshot) or run locally.

````

---

# 6) Step-by-step: exact commands (copy/paste)

## Local (Ubuntu / WSL)
```bash
# 1. clone repo (if not already)
git clone <your-repo-url>
cd face-hand-landmarks

# 2. system deps (fix libGL)
sudo apt update
sudo apt install -y libgl1 libglib2.0-0 ffmpeg

# 3. venv + install
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 4. run
streamlit run app.py
# open http://localhost:8501
````

## GitHub Codespaces

1. Push repo to GitHub.
2. Open repo → **Code → Open with Codespaces → New codespace**.
3. Wait for build (uses `.devcontainer`).
4. In Codespaces terminal:

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

5. Click forwarded port 8501 to open app in browser.

---

# 7) Important notes (read this)

* If you're running inside Codespaces and want **real-time camera** (server camera) you must attach a camera device to that container — that’s messy. The **recommended** workflow:

  * Use **Browser webcam (snapshot)** mode (works in browser → best UX, easy).
  * Or run the devcontainer locally (VS Code Remote - Containers) with access to `/dev/video0`.

* If you still see `ImportError: libGL.so.1`, run:

```bash
sudo apt-get update && sudo apt-get install -y libgl1
```

or use the devcontainer above which installs it for you.

---