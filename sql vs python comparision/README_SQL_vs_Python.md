# SQL vs Python: Data Analysis Comparison 🐍📊

This project demonstrates a **side-by-side comparison** between SQL and Python (Pandas) for performing various data analysis tasks on a dataset with 12,000+ rows.

## 📁 Dataset Overview
- 12,684 rows × 27 columns
- Contains attributes like `destination`, `passenger`, `weather`, `temperature`, `time`, `coupon`, `occupation`, etc.

## 🧠 What This Project Covers

| SQL Query | Equivalent Python Code (Pandas) |
|-----------|----------------------------------|
| SELECT col1, col2 FROM table | df[['col1', 'col2']] |
| SELECT * FROM table LIMIT 10 | df.head(10) |
| SELECT DISTINCT col FROM table | df['col'].unique() |
| SELECT * WHERE col='val' | df[df['col'] == 'val'] |
| ORDER BY col | df.sort_values('col') |
| GROUP BY col | df.groupby('col').size() |
| GROUP BY + AGG (SUM, AVG, MIN, MAX) | df.groupby('col')['num_col'].agg(['sum', 'mean', 'min', 'max']) |
| JOIN | pd.merge(df1, df2, on='col') |
| LIKE, IN, BETWEEN | .str.startswith(), .isin(), .between() |

## 🛠 Technologies Used
- Python 3.x
- Pandas
- Jupyter Notebook

## 📂 Notebook Link
- [View Full Notebook](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Comparision_Between_SQL_and_Python.ipynb)

## 👨‍🏫 Mentor
Special thanks to **Prakash Senapati Sir** for valuable guidance and mentorship.

## 🔗 Connect
If you're into **Data Science**, **Analytics**, or **Python**, feel free to connect and collaborate!

---

### 🔖 Tags
#Python #SQL #DataAnalysis #Pandas #EDA #DataScience #Comparison #GitHub #StudentProject #UnderGuidance
