# Titanic Survival Prediction

An end-to-end Python machine learning project for predicting passenger survival using the Titanic dataset. The project covers exploratory data analysis, data cleaning, feature engineering, model comparison, cross-validation, hyperparameter optimization, and model evaluation.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

## Project Workflow

The project is organized into three notebooks:

1. **Exploratory Data Analysis (`01_eda.ipynb`)**
   - Explore the Titanic dataset
   - Examine passenger and survival patterns
   - Investigate missing values and feature relationships
   - Visualize relevant trends

2. **Data Cleaning & Feature Engineering (`02_data_cleaning.ipynb`)**
   - Handle missing values
   - Encode categorical variables
   - Create additional predictive features
   - Prepare the dataset for machine learning

3. **Model Building & Evaluation (`03_model_building.ipynb`)**
   - Train and compare multiple classification models
   - Apply 5-fold cross-validation
   - Optimize Random Forest hyperparameters with GridSearchCV
   - Evaluate models using classification metrics and ROC curves

## Machine Learning Models

Seven classification models were implemented and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gradient Boosting
- Naive Bayes

## Feature Engineering

The preprocessing workflow includes:

- Group-based median imputation for missing Age values using Pclass and Sex
- Median imputation for Fare
- Mode imputation for Embarked
- Removal of Cabin, Name, Ticket, and PassengerId
- Categorical encoding
- Title extraction and rare-title grouping
- FamilySize calculation
- IsAlone indicator
- Age grouping
- Fare binning

Reusable preprocessing and feature-engineering functions are maintained in `utils.py`.

## Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve
- ROC-AUC
- 5-fold cross-validation

Random Forest hyperparameters are optimized using `GridSearchCV`, including tree depth, minimum samples for splitting and leaves, and number of estimators.

## Project Structure

```text
titanicsurvivor/
├── data/
│   └── titanic_cleaned.csv
│   └── titanic.csv
├── .gitignore
├── 01_eda.ipynb
├── 02_data_cleaning.ipynb
├── 03_model_building.ipynb   
├── README.md
├── requirements.txt
└── utils.py
```

## Environment Setup

Create a virtual environment:

```bash
python -m venv .myenv
```

### Windows

```bash
.myenv\Scripts\activate
```

### macOS / Linux

```bash
source .myenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter:

```bash
jupyter notebook
```

Run the notebooks in order:

```text
01_eda.ipynb
      ↓
02_data_cleaning.ipynb
      ↓
03_model_building.ipynb
```

## Reproducibility

Project dependencies are listed in `requirements.txt`. The Python virtual environment is intentionally excluded from Git using `.gitignore`.

## Notes

The notebooks use reusable helper functions in `utils.py` for data loading, feature engineering, preprocessing, model evaluation, cross-validation, confusion-matrix visualization, ROC analysis, and model comparison.
