# Data Preprocessing Pipeline with Scikit-Learn - Day 6 Challenge

In this challenge, we create a comprehensive data preprocessing pipeline for the Titanic dataset using Scikit-Learn’s `Pipeline` and `ColumnTransformer`. This modular approach ensures consistent and efficient preprocessing across different feature types, making it ideal for machine learning models.

---

## Challenge Outline

### 1. Set Up Data Types and Columns

- **Objective**: Separate columns into different types to apply the appropriate transformations.
- **Data Groups**:
  - **Numerical**: Columns such as `age`, `fare`, and `family_size`.
  - **Categorical**: Columns such as `embarked` and `pclass`.
  - **Binary**: Columns like `sex` and `is_alone`.

### 2. Define Transformation Steps

- **Numerical Columns**:

  - Use `SimpleImputer` with strategy='mean' to handle missing values.
  - Apply `StandardScaler` for feature scaling.

- **Categorical Columns**:

  - Use `SimpleImputer` with strategy='most_frequent' to fill missing values.
  - Apply `OneHotEncoder` to transform categorical features into binary vectors.

- **Binary Columns**:
  - **Label Encoding**: Encode binary columns (`sex` and `is_alone`) with values 0 and 1, if not already encoded.

### 3. Create the Pipeline

- **ColumnTransformer**:
  - Use `ColumnTransformer` to combine all preprocessing steps into a single pipeline.
  - Integrate individual transformers for numerical, categorical, and binary features.
  - Set `remainder='passthrough'` to retain any columns that are not explicitly transformed.

### 4. Test the Pipeline

- **Fit and Transform**:
  - Apply `fit_transform` to the Titanic dataset to generate a fully preprocessed dataset.
  - **Sample Output**: Display a sample of the transformed data to verify that each preprocessing step was applied correctly.

---
