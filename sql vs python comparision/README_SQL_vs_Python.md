# 🐍 SQL vs. Python: The Data Analysis Face-Off 📊

### 🎯 Project Overview

In the world of Data Science, there is often more than one way to solve a problem. This project provides a **comprehensive, side-by-side comparison** of SQL queries and Python (Pandas) code. Using a robust dataset of over **12,000+ rows**, I demonstrate how the two most essential tools in a data analyst's toolkit tackle the same challenges.

---

## 📂 Dataset Snapshot

The analysis is performed on a rich dataset featuring consumer behavior and environmental factors.

* **Scale:** 12,684 Rows × 27 Columns
* **Key Features:** `Destination`, `Passenger`, `Weather`, `Temperature`, `Time`, `Coupon`, `Occupation`.

---

## 🧠 Translation Guide: SQL to Pandas

This project serves as a "Rosetta Stone" for data professionals. Whether you are a SQL expert learning Python or vice versa, this mapping covers the essentials:

| Operation | SQL Syntax | Pandas Equivalent |
| --- | --- | --- |
| **Selection** | `SELECT col1, col2` | `df[['col1', 'col2']]` |
| **Preview** | `LIMIT 10` | `df.head(10)` |
| **Uniques** | `SELECT DISTINCT col` | `df['col'].unique()` |
| **Filtering** | `WHERE col = 'val'` | `df[df['col'] == 'val']` |
| **Sorting** | `ORDER BY col DESC` | `df.sort_values('col', ascending=False)` |
| **Grouping** | `GROUP BY col` | `df.groupby('col').size()` |
| **Aggregation** | `SUM(col), AVG(col)` | `df.groupby('col').agg(['sum', 'mean'])` |
| **Merging** | `JOIN table_b ON ...` | `pd.merge(df_a, df_b, on='col')` |

---

## 🛠️ Tech Stack & Environment

* **Language:** Python 3.x
* **Library:** Pandas (for data manipulation)
* **Platform:** Jupyter Notebook / GitHub

---

## 🚀 Deep Dive into the Code

Want to see the logic in action? You can explore the full comparison, including complex filters and aggregations, in the interactive notebook:

👉 **[View Full Jupyter Notebook](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Comparision_Between_SQL_and_Python.ipynb)**

---

## 🎓 Mentorship

A special note of gratitude to **Prakash Senapati Sir** for providing the guidance and industry insights necessary to bring this comparison to life.

## 🤝 Connect & Collaborate

I’m always looking to connect with fellow Data Science enthusiasts and professionals.

* **GitHub:** [@Tanmay1112004](https://www.google.com/search?q=https://github.com/Tanmay1112004)
* **Keywords:** #Python #SQL #DataAnalysis #Pandas #EDA #DataScience

---
