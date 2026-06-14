# 🎭 Mood Classification using CNN

A **deep learning–based image classification project** that detects human mood as **Happy 😊** or **Sad 😢** using a **Convolutional Neural Network (CNN)**.
Developed with **TensorFlow/Keras** and deployed via **Gradio** for an intuitive, real-time web experience.

> Built for clarity, accuracy, and real-world usability.

---
## Demo Images

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/mood%20classifiction%20using%20Deep%20learnining%20-%20cnn/screenshots/Screenshot%202025-08-29%20224426.png)                                                                                                          ![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/mood%20classifiction%20using%20Deep%20learnining%20-%20cnn/screenshots/Screenshot%202025-08-29%20224855.png)

---

## 🚀 Key Features

* 🧠 **CNN-Based Image Classifier**
  Trained to distinguish between *Happy* and *Sad* facial expressions.

* 🔄 **Data Augmentation**
  Improves generalization and reduces overfitting.

* 🛑 **Early Stopping & Model Checkpointing**
  Ensures optimal model performance and training efficiency.

* 🌐 **Interactive Gradio Web App**
  Upload an image and get instant predictions.

* 📊 **Confidence-Aware Predictions**
  Displays probability scores alongside emoji-based results.

---

## 📂 Project Structure

```
mood-classification-cnn/
│── data/                          # Training & validation dataset (not included)
│── mood_classifier.ipynb          # Main notebook (Google Colab compatible)
│── best_mood_model.h5             # Saved trained CNN model
│── README.md                      # Project documentation
```

---

## ⚡ Live Demo (Recommended via Google Colab)

1. Open the notebook in **Google Colab**
2. Mount Google Drive and load the dataset
3. Train the CNN *or* load the saved model
4. Launch the **Gradio interface** for live predictions

Zero local setup. Smooth execution.

---

## 🧠 Model Architecture

* **Conv2D + MaxPooling** × 3
* **Dense (256 units)** + Dropout (0.4)
* **Output Layer:** Dense (1, Sigmoid)

**Training Configuration**

* Optimizer: `Adam`
* Loss Function: `binary_crossentropy`
* Evaluation Metric: `accuracy`

Balanced, lightweight, and effective for binary image classification.

---

## 📊 Results & Observations

* Consistent improvement in training accuracy with data augmentation
* Reduced overfitting due to dropout and early stopping
* Clear confidence scores for transparent predictions

---

## 🎨 Gradio Web Interface

* 📤 Upload a facial image
* ⚡ Instant mood classification
* 😊 / 😢 Emoji-based output
* 📈 Confidence score displayed for trust & explainability

Clean UX. No clutter. Straight to the point.

---

## 🔧 Setup Instructions (Local)

```bash
git clone https://github.com/Tanmay1112004/mood-classification-cnn.git
cd mood-classification-cnn
pip install -r requirements.txt
```

Alternatively, **Google Colab** is highly recommended for faster setup and GPU access.

---

## 📌 Requirements

* Python 3.10+
* TensorFlow 2.x
* Gradio
* Pillow
* NumPy

Install manually using:

```bash
pip install tensorflow gradio pillow numpy
```

---

## 📜 License

MIT License © 2025
Developed with ❤️ by **Tanmay**

---

## 🤝 Contributions

Pull requests are welcome.
If you have ideas for:

* Multi-class emotion detection
* Model optimization
* UI improvements

Let’s build it together.

---

> 💡 **Pro Tip:** Use clear, front-facing images for best prediction accuracy.
> This model rewards clean data. Clean data wins. 🚀
