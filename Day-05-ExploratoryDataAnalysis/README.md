# Exploratory Data Analysis (EDA) and Feature Engineering on Titanic Dataset - Day 5 Challenge

In this challenge, we perform an in-depth exploratory data analysis and create new features to enhance our understanding of the Titanic dataset. The goal is to uncover relationships and patterns that may improve model performance. The steps and code are implemented in the attached Jupyter notebook (`eda_fe_titanic.ipynb`).

---

## Challenge Outline

### 1. Analyze Relationships between Variables
- **Objective**: Investigate how variables such as `age`, `fare`, `pclass`, and `sex` relate to survival.
- **Visualizations**:
    - Use histograms, bar plots, and box plots to visualize these relationships.
    - Libraries: Primarily `seaborn` (e.g., `sns.histplot()`, `sns.boxplot()`, and `sns.countplot()`) and `matplotlib`.

### 2. Feature Engineering
- **Create New Features**:
    - **Family Size**: Combine `sibsp` (siblings/spouses) and `parch` (parents/children) to create a new feature, `family_size`.
    - **Is Alone**: Use `family_size` to create a binary feature indicating whether a passenger was alone or not.
    - **Fare per Person**: Create a new feature as the `fare` divided by `family_size`.
    - **Age Group**: Use `pd.cut()` to bin the `age` feature into categories such as "Child," "Teenager," "Adult," and "Senior."

- **Label Encoding**:
    - Encode `sex` and `embarked` to numerical values for use in machine learning models.

### 3. Visualize Feature Distributions and Relationships
- **Pairwise Relationships**:
    - Use `sns.pairplot()` to observe pairwise relationships between features.
    - Use `sns.heatmap()` to visualize the correlation matrix and understand relationships between engineered features and the target variable (`survived`).

- **Compare Survival Rates**:
    - Visualize survival rates across different bins and categories of the newly created features to assess their impact on survival.

### 4. Outlier Handling
- **Outlier Detection**:
    - Use the Interquartile Range (IQR) method to detect outliers in `fare` and `age`.
    - Outliers are defined as values outside the range \([Q1 - 1.5 \times IQR, Q3 + 1.5 \times IQR]\).
  
- **Outlier Treatment**:
    - Cap extreme outliers to the nearest non-outlier values to reduce the influence of anomalous data points.

---

## Hints and Tips
- For **family_size**, calculate by adding `sibsp` and `parch`, then add 1 to count the passenger themselves.
- Use `pd.cut()` to create age groups and label encoding for categorical features.
- Refer to previous capping functions for handling extreme outliers effectively.

---

## How to Use
Open and run the `eda_fe_titanic.ipynb` notebook to go through the steps of EDA, feature engineering, and outlier handling. Each cell contains code and explanations for each task.

