import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def load_data(self):
        try:
            if self.file_path.endswith('.csv'):
                df = pd.read_csv(self.file_path)
            elif self.file_path.endswith('.xlsx'):
                df = pd.read_excel(self.file_path)
            else:
                raise ValueError("Unsupported file format")
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
            
    def split_data(self, df, target_col, test_size=0.2, random_state=42):
        X = df.drop(target_col, axis=1)
        y = df[target_col]
        return train_test_split(X, y, test_size=test_size, random_state=random_state)