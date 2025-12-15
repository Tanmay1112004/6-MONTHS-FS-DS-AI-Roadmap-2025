
# 🤖 EDA Automation using LLM Frameworks (Mistral, Ollama, Gradio UI)

This project demonstrates **automated Exploratory Data Analysis (EDA)** using **Large Language Models** (LLMs) like **Mistral** and **Ollama**, integrated with a **Gradio web interface** for an interactive and user-friendly experience.

## 🚀 Live Demo
![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/EDA%20Automation%20using%20llm%20framework's%20-%20mistral%2C%20ollama%2C%20gradio%20ui/screen%20shots/Screenshot%202025-07-26%20214938.png)                                                                       ![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/EDA%20Automation%20using%20llm%20framework's%20-%20mistral%2C%20ollama%2C%20gradio%20ui/screen%20shots/Screenshot%202025-07-26%20214955.png)

## 🛠️ Technologies Used
- 🧠 **Mistral** - for generating insights from data summary
- 🧠 **Ollama** - for running models locally
- 🎛️ **Gradio** - for creating a simple and beautiful UI
- 📊 **Pandas** - for data manipulation and summary statistics

## 📂 Project Structure

```
EDA-LLM-Automation/
├── app.ipynb                     # Jupyter Notebook (main app)
├── README.md                    # Project Documentation
├── requirements.txt             # Required libraries
└── images/
    ├── gradio_ui.png            # UI Screenshot (optional)
    └── eda_output.png           # Output Summary Screenshot (optional)
```

## 📸 Screenshots

### 🖥️ Gradio UI
![Gradio UI](images/gradio_ui.png)

### 📊 EDA Output
![EDA Output](images/eda_output.png)

## 🧪 How It Works
1. Upload a CSV file using the Gradio UI.
2. The app reads the file and generates a summary using `pandas.describe()`.
3. Mistral or Ollama LLM interprets this summary to generate natural language insights.
4. Results are shown on the web interface.

## 📦 Installation

### Locally using VS Code

```bash
git clone https://github.com/your-username/eda-llm-automation.git
cd eda-llm-automation
pip install -r requirements.txt
python app.py
```

### Google Colab
Just open the notebook and run all cells.

## 🤖 Requirements

- Python 3.8+
- pandas
- gradio
- ollama (locally installed)
- mistral (optional, uses space)

## 🧠 Future Improvements

- Add more visualization features using matplotlib/seaborn/plotly
- Support for Excel files
- Natural Language Query Support

## 👨‍💻 Author
**Tanmay Kahirsagar**

---
⭐ Don't forget to **star** the repo if you find it helpful!
