# VNSGU Student Results - Data Analytics Project

A comprehensive data analytics project analyzing student performance data from Veer Narmad South Gujarat University (VNSGU). This project includes data loading, exploratory data analysis (EDA), preprocessing, and K-Means clustering to uncover insights into student performance patterns.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Workflow](#workflow)
- [Technologies Used](#technologies-used)
- [Output Files](#output-files)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Overview

This project performs comprehensive data analytics on VNSGU university student results using a structured workflow:

1. **Data Loading**: Import and initial exploration of raw student data
2. **Exploratory Data Analysis (EDA)**: Statistical analysis and visualization
3. **Data Preprocessing**: Cleaning, handling missing values, and feature engineering
4. **K-Means Clustering**: Grouping students based on performance patterns

The analysis is organized into separate Jupyter notebooks for each stage, ensuring a clean and maintainable workflow.

---

## Features

- [+] **Modular Notebook Structure** - Each analysis phase in separate notebooks
- [+] **Comprehensive EDA** with detailed visualizations
- [+] **Advanced Data Preprocessing** pipeline
- [+] **K-Means Clustering** for student segmentation
- [+] **Statistical Analysis** and correlation studies
- [+] **Rich Visualizations** using Matplotlib and Seaborn
- [+] **Organized Data Management** with raw and processed folders
- [+] **Model Storage** for trained clustering models
- [+] **Virtual Environment** for dependency isolation

---

## Project Structure

```
Data-Analytics-using-Python-Minor-Project/
�
+-- Data/                              # Data directory
�   +-- raw/                           # Raw data files
�   �   +-- VNSGU_Results.xlsx        # Original student results dataset
�   +-- processed/                     # Cleaned and processed data
�       +-- cleaned_student_data.xlsx  # Preprocessed data (generated)
�
+-- Notebooks/                         # Jupyter notebooks for analysis
�   +-- 01_data_loading.ipynb         # Load and explore raw data
�   +-- 02_eda.ipynb                  # Exploratory Data Analysis
�   +-- 03_preprocessing.ipynb        # Data cleaning and preprocessing
�   +-- 04_kmeans_clustering.ipynb    # K-Means clustering analysis
�
+-- models/                            # Trained models storage
�   +-- (clustering models will be saved here)
�
+-- outpurs/                           # Analysis outputs
�   +-- (visualizations and reports will be saved here)
�
+-- main.ipynb                         # Main notebook (optional entry point)
+-- requirements.txt                   # Python package dependencies
+-- README.md                          # Project documentation (this file)
+-- .gitignore                         # Git ignore configuration
+-- venv/                              # Virtual environment (auto-generated)
```

---

## Prerequisites

### Required Software

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Visual Studio Code** ([Download](https://code.visualstudio.com/))
- **Git** (Optional, for version control)

### Required VS Code Extensions

Install these extensions in VS Code (Press `Ctrl + Shift + X` to open Extensions):

1. **Python** (by Microsoft) - Essential for Python development
2. **Jupyter** (by Microsoft) - Required to run .ipynb notebook files

> **Important**: Without these extensions, the notebook will not run in VS Code.

### Required Python Libraries

All dependencies are listed in `requirements.txt`:

```
pandas>=2.0.0          # Data manipulation and analysis
numpy>=1.24.0          # Numerical computing
matplotlib>=3.7.0      # Data visualization
seaborn>=0.12.0        # Statistical data visualization
openpyxl>=3.1.0        # Excel file reading/writing
sweetviz>=2.3.0        # Automated EDA report generation
ipykernel>=6.25.0      # Jupyter kernel for VS Code
```

---

## Installation & Setup

### Step 1: Clone or Download the Project

```bash
# If using Git
git clone <repository-url>
cd VNSGU_Data

# Or download and extract the ZIP file
```

### Step 2: Open in VS Code

1. Open **Visual Studio Code**
2. Go to **File ? Open Folder**
3. Select the `VNSGU_Data` folder
4. VS Code will load the entire project

### Step 3: Install Python Extensions

1. Press `Ctrl + Shift + X` to open Extensions
2. Search for **"Python"** and install the extension by Microsoft
3. Search for **"Jupyter"** and install the extension by Microsoft
4. Restart VS Code if prompted

### Step 4: Set Up Virtual Environment (Recommended)

Using a virtual environment ensures isolated package management and prevents dependency conflicts.

**Option A: Automatic Setup (if venv folder doesn't exist)**

Open the integrated terminal in VS Code (`Ctrl + ` ` or **Terminal ? New Terminal**) and run:

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

**Option B: Quick Setup (if venv already exists)**

```powershell
# Activate the existing virtual environment
.\venv\Scripts\activate

# Install/update dependencies
pip install -r requirements.txt
```

**For Linux/Mac:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 5: Select Python Interpreter in VS Code

1. Press `Ctrl + Shift + P` to open Command Palette
2. Type **"Python: Select Interpreter"**
3. Select the interpreter from `.\venv\Scripts\python.exe` (Windows) or `./venv/bin/python` (Linux/Mac)
4. This ensures VS Code uses the virtual environment

> **Tip**: Once activated, you'll see `(venv)` prefix in your terminal prompt.

### Alternative: Without Virtual Environment

If you prefer not to use a virtual environment (not recommended):

```bash
pip install -r requirements.txt
```

---

## How to Run

### Quick Start

1. **Open the Project in VS Code**
   - Open Visual Studio Code
   - Go to **File ? Open Folder**
   - Select the `Data-Analytics-using-Python-Minor-Project` folder

2. **Set Up Python Environment**
   ```powershell
   # Activate virtual environment
   .\venv\Scripts\activate
   
   # Install dependencies (if not already installed)
   pip install -r requirements.txt
   ```

3. **Select Python Interpreter**
   - Press `Ctrl + Shift + P` in VS Code
   - Type **"Python: Select Interpreter"**
   - Select the interpreter from `.\venv\Scripts\python.exe`

### Running the Notebooks

The analysis follows a sequential workflow. Run the notebooks in order:

#### **Notebook 1: Data Loading** (`01_data_loading.ipynb`)
- Loads the raw Excel data from `Data/raw/VNSGU_Results.xlsx`
- Performs initial data exploration
- Displays dataset structure and dimensions

#### **Notebook 2: Exploratory Data Analysis** (`02_eda.ipynb`)
- Statistical analysis and summary statistics
- Data distribution analysis
- Correlation studies
- Visualization of key patterns and trends
- Subject-wise performance analysis

#### **Notebook 3: Data Preprocessing** (`03_preprocessing.ipynb`)
- Handles missing values
- Removes irrelevant columns
- Data standardization and normalization
- Feature engineering
- Saves cleaned data to `Data/processed/cleaned_student_data.xlsx`

#### **Notebook 4: K-Means Clustering** (`04_kmeans_clustering.ipynb`)
- Loads preprocessed data
- Applies K-Means clustering algorithm
- Groups students based on performance patterns
- Visualizes clusters and analyzes characteristics
- Saves trained models to `models/` directory

### Running a Notebook

1. Open any notebook (e.g., `Notebooks/01_data_loading.ipynb`)
2. Select Python Kernel (top-right corner)
3. Run cells:
   - **Run All**: Click "Run All" button
   - **Run Single Cell**: Click ? button or press `Shift + Enter`

---

## Workflow

The project follows a systematic data analytics pipeline:

```
Raw Data ? Loading ? EDA ? Preprocessing ? Clustering ? Insights
```

1. **[>] Data Loading**: Import raw Excel data and explore structure
2. **[>] EDA**: Analyze patterns, distributions, and correlations
3. **[>] Preprocessing**: Clean data, handle missing values, feature engineering
4. **[>] Clustering**: Apply K-Means to segment students by performance
5. **[>] Insights**: Interpret results and visualize findings

---

## Technologies Used

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Python 3.x** | Primary programming language | 3.8+ |
| **Pandas** | Data manipulation and analysis | =2.0.0 |
| **NumPy** | Numerical computations | =1.24.0 |
| **Matplotlib** | Basic plotting and visualization | =3.7.0 |
| **Seaborn** | Statistical data visualization | =0.12.0 |
| **OpenPyXL** | Reading/writing Excel files | =3.1.0 |
| **Scikit-learn** | Machine learning (K-Means clustering) | Latest |
| **IPyKernel** | Jupyter kernel for VS Code | =6.25.0 |
| **Jupyter** | Interactive notebook environment | - |
| **VS Code** | Integrated development environment | Latest |

---

## Output Files

### Generated Files

1. **`Data/processed/cleaned_student_data.xlsx`**
   - Cleaned and preprocessed dataset
   - Ready for machine learning analysis
   - Missing values handled, irrelevant columns removed

2. **`models/` directory**
   - Trained K-Means clustering models
   - Model parameters and configurations
   - Can be loaded for future predictions

3. **`outpurs/` directory**
   - Visualizations and plots
   - Analysis reports
   - Charts and graphs generated during EDA

---

## ? Troubleshooting

### Common Issues and Solutions

#### ? **"ModuleNotFoundError: No module named 'pandas'"**
**Solution**: Activate virtual environment and install dependencies
```powershell
# Windows
.\venv\Scripts\activate
pip install -r requirements.txt

# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
```

#### ? **"Kernel not found" or "No kernel selected"**
**Solution**:
1. Make sure virtual environment is created and dependencies are installed
2. Press `Ctrl + Shift + P`
3. Type "Python: Select Interpreter"
4. Choose the interpreter from `.\venv\Scripts\python.exe`
5. Reopen the notebook

#### ? **"PermissionError: [Errno 13] Permission denied" when saving Excel**
**Solution**:
- Close the Excel file if it's open in Microsoft Excel or another program
- The file must not be locked by another process
- Make sure you have write permissions to the directory

#### ? **Virtual environment not activating**
**Solution (Windows)**:
```powershell
# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate again:
.\venv\Scripts\activate
```

#### ? **"FileNotFoundError: VNSGU_Results.xlsx"**
**Solution**: Ensure the Excel file is located at `Data/raw/VNSGU_Results.xlsx`

#### ? **Excel file not loading properly**
**Solution**:
```bash
pip install --upgrade openpyxl pandas
```

#### ? **Jupyter extension not working**
**Solution**:
1. Uninstall Python and Jupyter extensions
2. Restart VS Code
3. Reinstall both extensions
4. Restart VS Code again

#### ? **Plots not displaying**
**Solution**: Add this at the beginning of your notebook:
```python
%matplotlib inline
```

#### ? **Wrong Python interpreter selected**
**Solution**:
1. Check terminal - should show `(venv)` prefix
2. In notebook, click kernel selector (top-right)
3. Select the venv Python interpreter
4. Restart kernel if needed

---

## Managing Virtual Environment

### Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\activate
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Deactivate Virtual Environment

```bash
deactivate
```

### Update Dependencies

```bash
# Activate venv first
pip install --upgrade -r requirements.txt
```

### Add New Package

```bash
# Install new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

---

## Key Insights

This project demonstrates:

- **Data Pipeline Design**: Modular notebook structure for maintainability
- **Data Cleaning Techniques**: Handling missing values and data quality issues
- **Exploratory Analysis**: Statistical methods and visualization techniques
- **Machine Learning**: Unsupervised learning with K-Means clustering
- **Best Practices**: Version control, virtual environments, and documentation

---

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Set up virtual environment (`python -m venv venv`)
4. Activate and install dependencies (`pip install -r requirements.txt`)
5. Make your changes
6. Test your changes thoroughly
7. Update requirements.txt if you added new packages (`pip freeze > requirements.txt`)
8. Commit your changes (`git commit -am 'Add new feature'`)
9. Push to the branch (`git push origin feature/improvement`)
10. Create a Pull Request

---

## License

This project is open source and available for educational purposes.

---

## Contact & Support

For questions, suggestions, or issues:

- Open an issue in the repository
- Submit a pull request with improvements
- Contact the maintainer through GitHub

---

## Acknowledgments

- **VNSGU** for the dataset
- Python community for excellent data science libraries
- Contributors and maintainers of pandas, matplotlib, seaborn, and sweetviz
- Microsoft for VS Code and Python/Jupyter extensions

---

## Notes

- This is an educational project for learning data analysis with Python
- The dataset contains student performance data from VNSGU
- All analysis is performed using open-source tools
- The project demonstrates practical applications of EDA in education analytics
- Virtual environment is recommended for isolated dependency management
- All package versions are specified in `requirements.txt` for reproducibility

---

## License

This project is open source and available for educational purposes.

---

**Project Repository**: https://github.com/yugp5507/Data-Analytics-using-Python-Minor-Project
**Last Updated**: December 2025
**Python Version**: 3.8+
**Status**: Active

---

Made with  for Data Analytics Learning
