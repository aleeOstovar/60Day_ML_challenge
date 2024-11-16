# Feature Engineering and Encoding Categorical Variables - Day 4 Challenge

In this challenge, we enhance the Titanic dataset by creating new features and encoding categorical variables, essential steps in the data preprocessing pipeline for machine learning. The process is implemented in the provided Jupyter notebook (`FeatureEngineering.ipynb`).

---

## Objective
Learn to create and transform features in order to better represent patterns in the data, and encode categorical variables to make the dataset suitable for machine learning models.

---

## Tasks Overview

### 1. Load the Titanic Dataset
- **Dataset**: Continue with the cleaned Titanic dataset from Day 3. If not available, load the raw dataset and apply the same cleaning steps (handling missing values and outliers) before proceeding.

### 2. Feature Engineering
- **Creating New Features**:
    - **Family Size**: Combine `sibsp` (siblings/spouses aboard) and `parch` (parents/children aboard) to create a new feature called `family_size`.
    - **Is Alone**: Create a binary feature `is_alone`, where 1 indicates `family_size` is 0 (passenger is alone), otherwise 0.
    - **Title Extraction**: Extract titles (e.g., "Mr.", "Mrs.", "Miss.") from passenger names and store them in a new column, `title`.
  
- **Binning**:
    - **Age Grouping**: Bin the `age` column into categories such as "Child", "Teen", "Adult", and "Senior".
    - **Fare Discretization**: Categorize `fare` into "Low Fare," "Medium Fare," and "High Fare" groups.

### 3. Encoding Categorical Variables
- **One-Hot Encoding**:
    - Use one-hot encoding for nominal categorical columns, such as `embark_town` and the newly created `title`.
  
- **Label Encoding**:
    - Apply label encoding for ordinal categories, like the new `age_group` and `fare_group` bins, to preserve the natural ordering.

### 4. Correlation Analysis (Optional)
- **Correlation Matrix**: Check the correlation between your target variable (`survived`) and all other features.
- **Heatmap Visualization**: Use a heatmap to visualize correlations and identify any insights related to the new features.

### 5. Output Summary
- **Data Preview**: Print the first few rows of the transformed DataFrame to verify the transformations.
- **Summary**: Document the decisions for each feature engineering step and any noteworthy correlations observed.

---

## How to Use
Open and run the `FeatureEngineering.ipynb` file to follow the feature engineering and encoding steps. Each cell contains code and explanations for each part of the task.

Happy feature engineering!
