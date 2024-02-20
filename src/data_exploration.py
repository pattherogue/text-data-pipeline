import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the loaded data.
    """
    data = pd.read_csv(file_path)
    return data

def main():
    # Load data from CSV files
    train_data = load_data("../data/train_data.csv")
    valid_data = load_data("../data/valid_data.csv")

    # Display basic information about the datasets
    print("Train Data:")
    print(train_data.info())
    print("\nValid Data:")
    print(valid_data.info())

    # Display the first few rows of the datasets
    print("\nFirst few rows of Train Data:")
    print(train_data.head())
    print("\nFirst few rows of Valid Data:")
    print(valid_data.head())

    # Perform additional exploratory data analysis as needed

if __name__ == "__main__":
    main()
