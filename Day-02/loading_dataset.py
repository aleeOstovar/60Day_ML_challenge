# loading Iris dataset from sklearn
import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
import os

# Creating a pandas DataFrame from the loaded dataset
file_path = "./dataset/iris.csv"
if not os.path.exists(file_path):
    print('downloading Dataset...')
    iris = load_iris()
    store_iris = pd.DataFrame(
        data=np.c_[iris["data"], iris["target"]],
        columns=iris["feature_names"] + ["target"],
    ).to_csv("./dataset/iris.csv")
    


df = pd.read_csv("./dataset/iris.csv")
print(df)
