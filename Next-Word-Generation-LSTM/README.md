# 🎬 Next Word Generation using LSTM

A **Deep Learning–powered Next Word Prediction system** trained on the **TMDB 5000 Movies Dataset**.
This project leverages **LSTM (Long Short-Term Memory)** networks to predict and generate the next words in a sequence with contextual understanding.

To make it practical (and fun), the model is wrapped inside an **interactive Gradio web interface**, allowing real-time experimentation with text generation parameters.

---

## ✨ Highlights

* End-to-end **text preprocessing & tokenization**
* **LSTM-based neural network** for next-word prediction
* Training visualization with **loss & accuracy curves**
* Model persistence using `.h5` format
* **Interactive Gradio UI**

  * Adjustable number of predicted words
  * Top-K word selection for controlled randomness
* Sleek **dark-themed demo interface**

---

## 🧠 How It Works (High Level)

1. Movie titles are tokenized and converted into sequences
2. LSTM learns word dependencies and contextual patterns
3. Given a seed phrase, the model predicts the most probable next words
4. Gradio provides a real-time playground to test predictions

Simple pipeline. Solid ML fundamentals. Clean execution.

---

## 📂 Project Structure

```
├── Next_Word_Prediction.ipynb    # Colab notebook (training + inference)
├── nwp.h5                       # Trained LSTM model
├── tmdb_5000_movies.csv         # Dataset (from Kaggle)
└── README.md                    # Project documentation
```

---

## 🛠️ Tech Stack

* **Python** 🐍
* **TensorFlow / Keras**
* **Pandas & NumPy**
* **Gradio** (Interactive frontend)
* **Matplotlib** (Training visualizations)

---

## ⚡ Quick Start

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Tanmay1112004/Next-Word-Generation-LSTM.git
cd Next-Word-Generation-LSTM
```

### 2️⃣ Open in Google Colab

Upload:

* Notebook
* Dataset
* Model file (`nwp.h5`)

### 3️⃣ Install dependencies

```bash
!pip install tensorflow gradio matplotlib pandas numpy
```

### 4️⃣ Run all cells

Train (or load) the model and initialize the UI.

### 5️⃣ Launch the Gradio app

```python
demo.launch(share=True)
```

Boom. Live demo ready 🚀

---

## 🎯 Sample Prediction

**Seed Text**

```
The Lord
```

**Model Output (Next 5 Words)**

```
The Lord of the Rings
```

Clean prediction. Context locked in 🔐

---

## 📊 Training Insights

* Accuracy and loss curves are plotted directly in the notebook
* Helps monitor convergence and detect overfitting early

This keeps the model honest and production-ready.

---

## 📌 Use Cases

* Text autocomplete systems
* NLP learning projects
* Language modeling experiments
* AI-powered content tools

---

## 🤝 Acknowledgements

* **Dataset:** TMDB 5000 Movies Dataset (Kaggle)
  [https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## ⭐ Support

If this project helped you:

* **Star the repository**
* Share feedback
* Connect with me on **LinkedIn**
  👉 [https://www.linkedin.com/tanmay-kshirsagar](https://www.linkedin.com/tanmay-kshirsagar)

Let’s build smarter NLP systems — one word at a time 💡🔥

---

