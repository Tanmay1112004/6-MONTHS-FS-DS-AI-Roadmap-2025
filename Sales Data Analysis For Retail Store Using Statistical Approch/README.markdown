# 📊 Sales Data Analysis for Retail Store 🛒

> **Transforming raw retail data into actionable business insights using statistics & visualization**

---

## 🚀 Overview

In a data-driven retail environment, understanding sales patterns is critical for optimizing **inventory, pricing, and marketing strategies**.

This project delivers an **end-to-end statistical analysis pipeline** using Python to uncover trends, validate assumptions, and visualize performance across multiple product categories.

---

## 🎯 Business Objective

The goal of this project is to simulate real-world retail analytics by:

* 📈 Analyzing **sales distribution patterns**
* 🔍 Performing **statistical hypothesis testing**
* 📊 Generating **visual insights for decision-making**

---

## 🗂 Dataset Overview

A synthetic dataset representing retail sales activity:

| Feature        | Description                               |
| -------------- | ----------------------------------------- |
| `product_id`   | Unique product identifier                 |
| `product_name` | Product label                             |
| `category`     | Electronics, Clothing, Home, Sports       |
| `units_sold`   | Sales volume (Poisson distribution, λ=20) |
| `sale_date`    | Transaction date (Jan 1–20, 2023)         |

📌 **Scope:**

* 20 products
* 4 categories
* Time-based sales simulation

---

## 🧠 Analytical Approach

### 📈 Descriptive Statistics

* Mean, Median, Mode → Identify central trends
* Variance & Standard Deviation → Measure dispersion
* Category-wise aggregation → Performance comparison

---

### 📉 Inferential Statistics

* **Confidence Intervals (95%, 99%)** → Estimate population mean
* **One-Sample T-Test** → Validate if average sales differ from expected value (μ = 20)

---

### 📊 Data Visualization

* 📈 **Histogram** → Distribution of units sold
* 📊 **Boxplot** → Category-wise variability & outliers
* 📉 **Bar Chart** → Total sales comparison across categories

---

## 📊 Key Insights

* 📌 Average sales (~18.8 units) are **close to expected baseline (20)**
* 📌 High-performing category: **Home products**
* 📌 Sales variability exists across categories → indicates **demand fluctuation**
* 📌 Hypothesis testing confirms:
  👉 No statistically significant deviation from expected sales

---

## 🛠️ Tech Stack

| Layer           | Technology          |
| --------------- | ------------------- |
| Language        | Python 🐍           |
| Data Processing | Pandas, NumPy       |
| Visualization   | Matplotlib, Seaborn |
| Statistics      | SciPy               |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/Retail-Sales-Analysis.git
cd Retail-Sales-Analysis
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Project

```bash
python sales_data_analysis.py
```

---

## 📂 Project Structure

```
├── sales_data_analysis.py   # Core analysis script
├── sales_data.csv           # Synthetic dataset
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

---

## 📈 Sample Results

```
Mean Units Sold: 18.80  
Median Units Sold: 18.50  
Mode Units Sold: 17  
Standard Deviation: 3.30  
```

📊 **95% Confidence Interval:**

```
(17.25, 20.35)
```

🧪 **Hypothesis Test Result:**

```
P-value: 0.12  
→ Fail to reject null hypothesis
```

---

## 💡 Business Impact

This project demonstrates how statistical analysis can:

* Improve **inventory planning**
* Enable **data-backed decision making**
* Identify **high-performing product categories**
* Reduce uncertainty using **confidence intervals & hypothesis testing**

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork, improve, and submit a pull request 🚀

---

## 📜 License

Licensed under the **MIT License**

---

## 📬 Connect

👨‍💻 **Tanmay Kshirsagar**
💼 Open to Data Science, Analytics & ML Opportunities

---

## ⭐ Final Note

If this project helped you or inspired your learning, consider giving it a ⭐

---
