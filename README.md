# 🛒 E-Commerce ML & AI SQL Analyst Agent Portfolio

An end-to-end Data Engineering, Predictive Machine Learning, and Agentic AI solution. This project transforms raw e-commerce data stored in MySQL into interactive business intelligence dashboards, predicts customer churn risk using Scikit-Learn, and exposes an interactive AI Analyst Agent powered by LangChain and Groq LLM to query the database using natural language.

---

## 📌 Executive Summary & Business Value

* **Phase 1 (Data Engineering & BI):** Extracted, cleaned, and modeled relational e-commerce data from MySQL into an executive Power BI dashboard tracking revenue, order count, and customer activity.
* **Phase 2 (Predictive Machine Learning):** Engineered customer aggregation features and trained a Scikit-Learn model to predict churn probability, exporting predictions back into MySQL to enable proactive customer retention.
* **Phase 3 (Agentic AI Systems):** Built a zero-shot SQL Agent that translates natural language business questions into dynamic SQL queries, executes them on MySQL, and summarizes the results in plain English.

---

## 🛠️ Tech Stack & Tools Used

### **Data Engineering & Database Management**
* **MySQL Server & Workbench:** Relational database management system storing core tables (`customers`, `products`, `orders`) and ML output tables (`churn_predictions`).
* **SQLAlchemy & mysql-connector-python:** Object Relational Mapper (ORM) and database drivers bridging Python with MySQL.
* **Pandas:** Data extraction, manipulation, aggregation, and ETL processing.

### **Data Visualization & Business Intelligence**
* **Power BI Desktop:** Interactive dashboard featuring KPI cards, revenue breakdowns by category, and churn overview donut charts connected directly to MySQL via Import mode.
* **Matplotlib & Seaborn:** Programmatic feature importance and ML evaluation chart generation.

### **Machine Learning & Predictive Analytics**
* **Scikit-Learn:** Feature preprocessing (`get_dummies`), dataset splitting, and model training using **Random Forest Classifier** and **Logistic Regression**.
* **NumPy:** Numerical arrays and score calculations.

### **Agentic AI & LLM Systems**
* **LangChain & LangChain-Community:** Framework for building tool-calling agent executors (`create_sql_agent`, `SQLDatabase`).
* **Groq API (`ChatGroq`):** High-speed LLM inference provider powering **Llama 3.3 (70B Versatile)** for dynamic SQL generation.
* **python-dotenv:** Secure environment configuration management for private API keys.

---

## 🏗️ Project Architecture & Workflow

```text
[ MySQL Database ]
       │
       ├──> (Phase 1: Pandas ETL) ──────> [ Power BI Dashboard ]
       │
       ├──> (Phase 2: Scikit-Learn ML) ─> [ Prediction Scores ] ──┐
       │                                                         │
       │ <──────────────────────── (Export Predictions) ─────────┘
       │
       └──> (Phase 3: LangChain + Groq) <─> [ Interactive Terminal Agent ]