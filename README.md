# 📊 Data Analytics using Python – Minor Project

This project focuses on **Exploratory Data Analysis (EDA)** using Python to analyze restaurant data and understand customer preferences and trends.

---

## 📌 Project Objective

The main goal of this project is to:

- ✅ Identify popular restaurant categories
- ✅ Analyze customer ratings and votes
- ✅ Compare online vs offline ordering trends
- ✅ Understand cost preferences for dining
- ✅ Perform univariate, bivariate, and multivariate analysis
- ✅ Generate actionable insights through data visualization

---

## 📋 Table of Contents

- [Project Objective](#-project-objective)
- [Project Setup Guide](#-project-setup-guide-step-by-step)
- [Project Structure](#-project-structure)
- [Project Features](#-project-features)
- [Key Insights](#-key-insights)
- [Common Issues & Fixes](#-common-issues--fixes)
- [Tech Stack](#-tech-stack)
- [Analysis Workflow](#-analysis-workflow)
- [Author](#-author)
- [Support](#-support)

---

## 🚀 Project Setup Guide (Step-by-Step)

### 📁 Step 1: Clone Repository

```bash
git clone https://github.com/yugp5507/Data-Analytics-using-Python-Minor-Project.git
cd Data-Analytics-using-Python-Minor-Project
```

### 🐍 Step 2: Install Python

- **Download Python:** https://www.python.org/downloads/
- **Recommended Version:** Python 3.10 or 3.11
- ⚠️ Make sure to check **"Add Python to PATH"**

**Check version:**
```bash
python --version
```

### 🧪 Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### ⚡ Step 4: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### ⬆️ Step 5: Upgrade pip

```bash
pip install --upgrade pip
```

### 📦 Step 6: Install Required Libraries (Compatible Versions)

```bash
pip install seaborn==0.12.2 matplotlib==3.7.2 pandas==1.5.3 numpy==1.23.5 scikit-learn==1.3.0
```

### 📄 Step 7: (Optional) Create requirements.txt

Generate requirements file:
```bash
pip freeze > requirements.txt
```

Install later using:
```bash
pip install -r requirements.txt
```

### ▶️ Step 8: Run Project

**Run Python file:**
```bash
python main.py
```

**Run Jupyter Notebook:**
```bash
pip install notebook
jupyter notebook
```

### 🧠 Step 9: Check Kernel in VS Code

**Method 1:**
- Open `.ipynb` file
- Check top-right corner
- Example: `Python 3.10 (venv)`

**Method 2:**
- Press `Ctrl + Shift + P`
- Search: `Python: Select Interpreter`

**Method 3 (Code Check):**
```python
import sys
print(sys.executable)
```

### ✅ Step 10: Verify Installation

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("All libraries working ✅")
```

---

## 📂 Project Structure

```
Data-Analytics-using-Python-Minor-Project/
├── main.ipynb                                  # Main analysis notebook
├── requirements.txt                            # Project dependencies
├── README.md                                   # Project documentation
├── Charts/                                     # Generated visualizations
├── Data/
│   ├── raw/
│   │   └── VNSGU_SEM4_All_Student_Results.csv # Raw dataset
│   └── processed/
│       └── VNSGU_SEM4_All_Student_Results_Cleaned.csv # Cleaned dataset
├── Documentation/                              # Project documentation
├── Notebooks/
│   ├── 01_data_loading.ipynb                  # Data loading & exploration
│   ├── 02_preprocessing.ipynb                 # Data cleaning & preprocessing
│   ├── 03_graphs.ipynb                        # Data visualization
│   ├── 04_kmeans_clustering.ipynb             # Clustering analysis
│   └── SWEETVIZ_REPORT.html                   # Automated EDA report
├── outputs/
│   └── cluster_summary.csv                    # Clustering results
├── models/                                     # Trained models
└── src/
    └── predict.py                             # Prediction script
```

---

## 📊 Project Features

- 🔍 **Data Cleaning** – Handling missing values, formatting, and data validation
- 📈 **Univariate Analysis** – Countplot, histogram, distribution analysis
- 🔗 **Bivariate Analysis** – Groupby operations, scatter plots, line plots
- 🌐 **Multivariate Analysis** – Heatmap, correlation analysis
- 🎨 **Data Visualization** – Seaborn & Matplotlib for insightful graphics
- 🤖 **Clustering Analysis** – K-means clustering for customer segmentation
- 📊 **Automated EDA Report** – Sweetviz report generation

---

## 📈 Key Insights

- 🍽️ **Majority of restaurants** fall into the Dining category
- ⭐ **Dining restaurants** receive the highest votes
- 📱 **Most restaurants** do not accept online orders
- 🌟 **Ratings** mostly range between 3.5 to 4.0
- 💰 **Couples** prefer dining cost around ₹300
- 📊 **Online orders** receive better ratings than offline orders

---

## ⚠️ Common Issues & Fixes

### ModuleNotFoundError
**Cause:** Wrong kernel selected  
**Fix:** Select correct venv kernel using `Python: Select Interpreter`

### Graph Not Showing
**Solution:** Use `plt.show()` in your code

### Version Conflict
**Fix:**
```bash
pip install --upgrade seaborn matplotlib pandas numpy
```

### Kernel Not Found
**Solution:**
```bash
python -m ipykernel install --user --name venv --display-name "Python (venv)"
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Notebook:** Jupyter Notebook
- **EDA Automation:** Sweetviz

---

## 📊 Analysis Workflow

1. **Data Loading & Exploration** – Load raw data and understand structure
2. **Data Preprocessing** – Clean data, handle missing values, feature engineering
3. **Univariate Analysis** – Individual variable distributions
4. **Bivariate Analysis** – Relationships between two variables
5. **Multivariate Analysis** – Relationships among multiple variables
6. **Clustering** – Customer segmentation using K-means
7. **Insights & Recommendations** – Generate actionable business insights

---

## 👨‍💻 Author

**Yug Patel**  
GitHub: https://github.com/yugp5507

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements.

---

## 📝 License

This project is open source and available under the MIT License.

---

## ⭐ Support

If you found this project useful, please **star the repository** ⭐

**Want a portfolio-level upgrade?** 🔥 I can add:
- 🖼️ **Screenshots section** with key visualizations
- 🏷️ **Badges** (Python version, license, status)
- 🎬 **Live demo style README**
- 📄 **Resume description**
- 📊 **Results and findings section**

Just let me know!

---

**Last Updated:** March 2026  
**Status:** Active & Maintained ✅  
**Python Version:** 3.10+
