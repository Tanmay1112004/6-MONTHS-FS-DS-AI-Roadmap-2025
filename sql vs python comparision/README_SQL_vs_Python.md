# 🐍 SQL vs. Python: The Data Analysis Face-Off 📊

![Image](https://learn.microsoft.com/en-us/fabric/data-warehouse/media/sql-query-editor/sql-query-editor-overview.png)

![Image](https://dataplatform.cloud.ibm.com/docs/api/content/wsj/getting-started/images/gs-notebook-cell01.png?context=wx\&locale=en)

![Image](https://substackcdn.com/image/fetch/%24s_%21xeDw%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9e53e45-be96-45ff-a2d1-b037d0d25710_1618x804.png)

![Image](https://media.licdn.com/dms/image/v2/D4D22AQGWBdPAfhMQgA/feedshare-shrink_800/B4DZZl2cN7HIAg-/0/1745465494155?e=2147483647\&t=nMamyVFScKZogcD8knZSISAbWB1EtaYTH_SnuUoNUDM\&v=beta)

In Data Analytics, the same problem can often be solved using **multiple tools**.
Two of the most powerful tools are **SQL** and **Python** with **Pandas**.

This project provides a **side-by-side comparison** showing how both approaches solve common data analysis tasks using the same dataset.

Think of it as a **translation guide between SQL and Pandas**.

---

# 🎯 Project Overview

The goal of this project is to demonstrate how **core data operations** translate between SQL queries and Python data manipulation.

Key focus areas include:

* Data selection
* Filtering
* Sorting
* Grouping
* Aggregation
* Data merging
* Exploratory analysis

Using both tools side-by-side helps analysts understand **when to use SQL and when to use Python**.

---

# 📂 Dataset Snapshot

The analysis is performed on a dataset containing **consumer behavior and environmental context variables**.

| Property     | Details               |
| ------------ | --------------------- |
| Rows         | 12,684                |
| Columns      | 27                    |
| Domain       | Consumer behavior     |
| Dataset Size | Medium-scale analysis |

### Important Features

* `Destination`
* `Passenger`
* `Weather`
* `Temperature`
* `Time`
* `Coupon`
* `Occupation`

This variety allows meaningful **grouping, filtering, and aggregation exercises**.

---

# 🧠 SQL → Pandas Translation Guide

| Operation       | SQL                   | Pandas                                   |
| --------------- | --------------------- | ---------------------------------------- |
| Selection       | `SELECT col1, col2`   | `df[['col1','col2']]`                    |
| Preview         | `LIMIT 10`            | `df.head(10)`                            |
| Distinct Values | `SELECT DISTINCT col` | `df['col'].unique()`                     |
| Filtering       | `WHERE col='val'`     | `df[df['col']=='val']`                   |
| Sorting         | `ORDER BY col DESC`   | `df.sort_values('col', ascending=False)` |
| Grouping        | `GROUP BY col`        | `df.groupby('col').size()`               |
| Aggregation     | `SUM(), AVG()`        | `df.groupby().agg()`                     |
| Join            | `JOIN table_b`        | `pd.merge()`                             |

This comparison makes it easier for:

* SQL users learning Python
* Python users learning SQL
* Data analysts transitioning between tools

---

# 🛠 Tech Stack

* **Python**
* **Pandas**
* **Jupyter Notebook**
* GitHub for version control

---

# 🚀 Explore the Full Notebook

You can view the full side-by-side implementation here:

👉
[https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Comparision_Between_SQL_and_Python.ipynb](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Comparision_Between_SQL_and_Python.ipynb)

The notebook includes:

* Real queries
* Equivalent Pandas code
* Filtering examples
* Aggregation comparisons
* Practical use cases

---

# 🎓 Mentorship

Special thanks to **Prakash Senapati** for the guidance and industry insights that helped shape this comparison project.

---

# 🤝 Connect

If you're interested in **Data Analysis, Python, SQL, or Machine Learning**, let's connect.

**GitHub**
[https://github.com/Tanmay1112004](https://github.com/Tanmay1112004)

---

# 📌 Key Takeaway

Great data analysts know **both SQL and Python**.

* **SQL → best for databases & querying**
* **Python → best for analysis & modeling**

Master both, and you control the entire data pipeline.

---
