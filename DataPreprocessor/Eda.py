import pandas as pd
import numpy as np


class EDAAnalyzer:
    def __init__(self):
        self.summary_stats = None
        self.missing_stats = None

    def analyze(self, df):
        self.summary_stats = self._get_summary_stats(df)
        self.missing_stats = self._get_missing_stats(df)
        self.data_types = df.dtypes
        return self

    def _get_summary_stats(self, df):
        return df.describe()

    def _get_missing_stats(self, df):
        missing = pd.DataFrame(
            {
                "missing_count": df.isnull().sum(),
                "missing_percentage": (df.isnull().sum() / len(df)) * 100,
            }
        )
        return missing[missing["missing_count"] > 0]

    def get_report(self):
        return {
            "summary_statistics": self.summary_stats,
            "missing_values": self.missing_stats,
            "data_types": self.data_types,
        }
