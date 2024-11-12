from DataLoader import DataLoader



def main():
    # Load dataset
    loader = DataLoader('../dataset/titanic.csv')
    df = loader.load_data()
    df.head()

    # Perform EDA
    log("Performing EDA...")
    EDA.explore(data)

    # Handle missing values
    log("Handling missing values...")
    data = MissingValuesHandler.handle(data)

    # Outlier detection and treatment
    log("Detecting and treating outliers...")
    data = OutlierHandler.handle(data)

    # Feature scaling
    log("Scaling features...")
    data = FeatureScaler.scale(data)

    # Encoding categorical variables
    log("Encoding categorical variables...")
    data = CategoricalEncoder.encode(data)

    # Feature engineering
    log("Performing feature engineering...")
    data = FeatureEngineer.engineer(data)

    # Handle class imbalance
    log("Handling class imbalance...")
    data = ImbalanceHandler.handle(data, Config.TARGET_COLUMN)
    
    # Final visualization and checks
    log("Finalizing preprocessing steps and visualizing results...")
    visualize(data)

    log("Preprocessing completed successfully.")


if __name__ == "__main__":
    main()
