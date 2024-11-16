# Data Exploration and Visualization - Day 2 Challenge

In this challenge, we dive into data exploration by analyzing a real dataset. We will preprocess, explore, and visualize key patterns, which are vital skills for any machine learning workflow. This project is structured into five folders, each representing a different stage of the analysis process:

1. `01-loading-dataset/`
2. `02-data-preprocess/`
3. `03-statistical-analysis/`
4. `04-visualization-plt/`
5. `05-PCA/`

Each folder contains Python scripts or Jupyter notebooks to execute the respective tasks. The chosen dataset for this analysis is the popular **Iris dataset**.

---

## Folder Structure and Tasks

### 1. `01-loading-dataset/`
This folder contains scripts for loading the dataset. Tasks include:
- **Loading the Dataset**: Load the Iris dataset using `sklearn.datasets` or any dataset of your choice from a source like Kaggle.
- **Converting to DataFrame**: Convert the data to a Pandas DataFrame for easy manipulation and analysis.

### 2. `02-data-preprocess/`
This folder focuses on data preprocessing. Tasks include:
- **Handling Missing Values**: Check for missing values and handle them by either filling with the mean or dropping rows.
- **Normalization**: Normalize numerical columns so that each feature falls within the range [0, 1].
- **Adding New Feature**: Add a new column called `sepal_to_petal_ratio` to calculate the ratio of sepal length to petal length.

### 3. `03-statistical-analysis/`
This folder contains scripts for performing statistical analysis on the dataset. Tasks include:
- **Calculating Statistics**: Calculate the mean, median, variance, and standard deviation for each feature.
- **Correlation Analysis**: Calculate the correlation matrix for all features and identify which features are highly correlated.

### 4. `04-visualization-plt/`
This folder demonstrates data visualization using `matplotlib` and `seaborn`. Tasks include:
- **Pair Plot**: Create a pair plot to observe relationships between all pairs of features.
- **Box Plot**: Create a box plot to compare the distributions of each feature across different species.
- **Heatmap**: Generate a heatmap of the correlation matrix with annotations to show correlation values.

### 5. `05-PCA/`
This folder explores dimensionality reduction using Principal Component Analysis (PCA). The task includes:
- **PCA and Visualization**: Use `sklearn.decomposition.PCA` to reduce the data to 2 dimensions and visualize it with a scatter plot, coloring the points based on the species to observe class separation.

---

## How to Use
Each folder contains a `.py` file or Jupyter notebook with solutions for the respective tasks. Run these files individually to complete the steps in data exploration and visualization.

---

