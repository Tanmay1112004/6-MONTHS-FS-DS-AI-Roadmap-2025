# ✨ Gemini Vision App

**Gemini Vision App** is a sleek, user-friendly web application built with **Streamlit** and **Google Gemini 2.5 Flash**. It allows users to analyze images, ask questions, and get instant AI-powered insights with a modern, attractive interface.  

---

## 🚀 Features

- **Multimodal Analysis**: Upload an image + optional text prompt and let Gemini analyze it.  
- **Text-only Q&A**: Ask questions or prompts without images.  
- **Streaming Responses**: View AI responses in real-time.  
- **Beautiful UI**: Modern design with gradients, card-style response boxes, and responsive image previews.  
- **Sidebar Guide**: Clear instructions, app info, and branding.  
- **Tabs Layout**: Separate sections for Image Analysis, Text Q&A, and About.

---

## 🖼️ Screenshots

![Home page](https://github.com/Tanmay1112004/Generative-AI-Journey/blob/main/Generative-AI-Journey/projects/Google%20Gemini%20projects/Gemini-Vision-App/screenshots/Screenshot%202025-09-27%20194030.png)  
*Image Analysis tab with prompt and uploaded image.*

![Image](https://github.com/Tanmay1112004/Generative-AI-Journey/blob/main/Generative-AI-Journey/projects/Google%20Gemini%20projects/Gemini-Vision-App/screenshots/Screenshot%202025-09-27%20194348.png)  
*Text Q&A tab for pure chatbot experience.*

![Image to text](https://github.com/Tanmay1112004/Generative-AI-Journey/blob/main/Generative-AI-Journey/projects/Google%20Gemini%20projects/Gemini-Vision-App/screenshots/Screenshot%202025-09-27%20194411.png)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/gemini-vision-app.git
cd gemini-vision-app
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add your Google API key**

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

4. **Run the app**

```bash
streamlit run app.py --server.port 7860 --server.address 0.0.0.0
```

Open the forwarded port in your browser (GitHub Codespaces or local machine).

---

## 📝 Usage

1. Go to **Image Analysis** tab:

   * Upload an image (JPG/PNG).
   * Enter a prompt (optional).
   * Click **Analyze Image** → get AI response.

2. Go to **Text Q&A** tab:

   * Enter any question or prompt.
   * Click **Get Answer** → Gemini responds in real-time.

3. Check **About** tab for app details and future upgrades.

---

## 💻 Tech Stack

* **Python**
* **Streamlit** (UI framework)
* **Google Generative AI** (Gemini 2.5 Flash)
* **Pillow** (Image handling)
* **dotenv** (Environment variables)

---

## ⚡ Future Enhancements

* Dark/Light mode toggle
* Multi-image support
* Chat-style interface with message history
* Downloadable responses

---

## 📜 License

MIT License © 2025 Tanmay

---

## 📫 Contact

For any questions or collaborations: [Tanmay GitHub](https://github.com/Tanmay1112004)

```
