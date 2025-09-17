# 🎬 Next Word Generation using LSTM  

This project is a **Next Word Prediction Model** trained on the **TMDB 5000 Movies dataset**.  
It uses **LSTM (Long Short-Term Memory)** neural networks to generate the next words in a sequence.  
The project also features an **interactive Gradio-based frontend** where you can test the model in real time.  

---

## 🚀 Features
- Preprocessing & tokenization of TMDB movie titles  
- LSTM-based text generation model  
- Training with accuracy/loss plots  
- Save & load trained model (`.h5` file)  
- **Gradio frontend** with sliders for number of words and top-k predictions  
- Clean **dark UI** for demo purposes  

---

## 📂 Project Structure
```

├── Next\_Word\_Prediction.ipynb   # Google Colab notebook (training + demo)
├── nwp.h5                       # Saved LSTM model
├── tmdb\_5000\_movies.csv         # Dataset (add via Kaggle/CSV)
└── README.md                    # Project documentation

````

---

## 🛠️ Tech Stack
- Python 🐍  
- TensorFlow / Keras  
- Pandas, NumPy  
- Gradio (for frontend UI)  
- Matplotlib (for plots)  

---

## ⚡ Quick Start

1. Clone this repository:
   bash
   git clone https://github.com/Tanmay1112004/Next-Word-Generation-LSTM.git
   cd Next-Word-Generation-LSTM


2. Open **Google Colab** and upload the notebook + dataset + model file.

3. Install dependencies inside Colab:

   ```bash
   !pip install tensorflow gradio matplotlib pandas numpy
   ```

4. Run all cells.

5. Launch the Gradio app:

   ```python
   demo.launch(share=True)
   ```

---

## 🎯 Example Output

**Seed text:**

```
The Lord
```

**Generated (next 5 words):**

```
The Lord of the Rings
```

---

## 📊 Training Curves

Loss and accuracy plots are included in the notebook for tracking training progress.

---

## 🤝 Acknowledgements

* Dataset: [TMDB 5000 Movies Dataset (Kaggle)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

⭐ If you like this project, don’t forget to **star the repo** and connect with me on [LinkedIn](https://www.linkedin.com/tanmay-kshirsagar)!

```
