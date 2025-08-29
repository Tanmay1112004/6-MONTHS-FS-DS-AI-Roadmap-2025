```markdown
# 🎭 Mood Classification with CNN  

A deep learning project that classifies moods as **Happy 😊** or **Sad 😢** using a **Convolutional Neural Network (CNN)**.  
Built with **TensorFlow/Keras** and deployed using **Gradio** for an interactive web demo.  

---

## 🚀 Features  
- CNN trained on custom Happy/Sad dataset.  
- Data augmentation for better generalization.  
- Early stopping & model checkpointing.  
- Interactive Gradio web app with image upload.  
- Confidence-based predictions with emoji labels.  

---

## 📂 Project Structure  
```

mood-classification-cnn/
│── data/                         # training & validation dataset (not uploaded here)
│── mood\_classifier.ipynb         # main notebook (Colab compatible)
│── best\_mood\_model.h5            # trained model (saved)
│── README.md                     # project documentation

````

---

## ⚡ Demo  
Run in **Google Colab**:  
1. Mount Google Drive and load dataset.  
2. Train the CNN or load saved model.  
3. Launch Gradio interface for predictions.  

---

## 🧠 Model Architecture  
- Conv2D → MaxPooling (x3)  
- Dense (256) + Dropout (0.4)  
- Dense (1, sigmoid)  

Optimizer: `Adam` | Loss: `binary_crossentropy` | Metrics: `accuracy`  

---

## 📊 Results  
- Training accuracy improves steadily with augmentation.  
- Confidence scores displayed for both moods.  

---

## 🎨 Gradio App UI  
- Upload a face image.  
- Get real-time classification: **😊 Happy / 😢 Sad**.  
- Confidence scores shown for transparency.  

---

## 🔧 Setup Instructions  
```bash
git clone https://github.com/your-username/mood-classification-cnn.git
cd mood-classification-cnn
pip install -r requirements.txt
````

Or run directly in **Google Colab** (recommended).

---

## 📌 Requirements

* Python 3.10+
* TensorFlow 2.x
* Gradio
* Pillow
* Numpy

Install with:

```bash
pip install tensorflow gradio pillow numpy
```

---
