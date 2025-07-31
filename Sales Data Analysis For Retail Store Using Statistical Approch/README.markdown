# 📊 Sales Data Analysis for Retail Store 🛒

## 🚀 Overview
Welcome to the **Sales Data Analysis for Retail Store** project! This Python-based analysis dives into retail sales data to uncover trends, test hypotheses, and visualize performance across product categories. Using statistical approaches, it empowers retail managers to make data-driven decisions for inventory and marketing strategies. 📈

## 📋 Project Description
In today’s competitive retail landscape, understanding sales performance is key to success. This project analyzes a synthetic dataset of 20 products across four categories—Electronics, Clothing, Home, and Sports—to achieve the following objectives:
- **Summarize Sales**: Compute descriptive statistics to understand sales distribution. 📉
- **Test Hypotheses**: Use inferential statistics to evaluate average sales against a target value. 🔍
- **Visualize Insights**: Create compelling visualizations for quick decision-making. 📊

## 🗃️ Dataset
The dataset is synthetically generated with the following features:
- **product_id**: Unique product identifier.
- **product_name**: Product name (e.g., Product 1, Product 2).
- **category**: Product category (Electronics, Clothing, Home, Sports).
- **units_sold**: Number of units sold (Poisson distribution, λ=20).
- **sale_date**: Date of sale (Jan 1–20, 2023).

## 📂 Repository Structure
- `sales_data_analysis.py`: Core Python script for data generation, analysis, and visualizations. 🐍
- `sales_data.csv`: Synthetic sales dataset. 📄
- `requirements.txt`: Required Python libraries. 📦
- `README.md`: You're reading it! 😊

## 🛠️ Installation
Get started in just a few steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/Retail-Sales-Analysis.git
   cd Retail-Sales-Analysis
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Dependencies: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`.
3. **Run the Analysis**:
   ```bash
   python sales_data_analysis.py
   ```

## 🔍 Analysis Breakdown
### 📈 Descriptive Statistics
- **Mean, Median, Mode**: Central tendencies of units sold.
- **Variance & Standard Deviation**: Variability in sales data.
- **Category Insights**: Total and average sales per category.

### 📉 Inferential Statistics
- **Confidence Intervals**: 95% and 99% intervals for the mean units sold. 🎯
- **Hypothesis Testing**: One-sample t-test to check if mean sales differ from 20 units. 🧪

### 📊 Visualizations
- **Histogram**: Distribution of units sold with mean, median, and mode lines. 📈
- **Boxplot**: Sales spread and outliers by category. 📊
- **Bar Plot**: Total units sold per category. 📉

## 🎉 Example Output
- **Descriptive Statistics**:
  ```
  Mean Units Sold: 18.80
  Median Units Sold: 18.50
  Mode Units Sold: 17
  Variance: 10.91
  Standard Deviation: 3.30
  ```
- **Category Statistics**:
  ```
     Category  Total Units Sold  Average Units Sold  Std Dev
  0  Clothing               21              21.00    NaN
  1  Electronics            73              18.25    2.22
  2  Home                  181              20.11    3.72
  3  Sports                101              16.83    2.71
  ```
- **Confidence Interval (95%)**:
  ```
  (17.25, 20.35)
  ```
- **Hypothesis Test**:
  ```
  T-statistic: -1.63, P-value: 0.12
  Fail to reject null hypothesis: Mean sales not significantly different from 20.
  ```

## 🖼️ Visualizations
The script generates:
- **Histogram**: Shows sales distribution with marked mean, median, and mode.
- **Boxplot**: Highlights sales variability across categories.
- **Bar Plot**: Compares total sales by category.

## 🤝 Contributing
We welcome contributions! 🌟 Fork the repo, make your changes, and submit a pull request. Let’s make this project even better together!

## 📜 License
This project is licensed under the [MIT License](LICENSE). 📝

## 📬 Contact
Questions or feedback? Open an issue or reach out on GitHub! 😄

---

**Built with 💻 and ❤️ for data-driven retail insights!**