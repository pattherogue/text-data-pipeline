import pandas as pd
import re

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

def preprocess_text(text):
    """
    Preprocess text data by removing special characters and converting to lowercase.

    Args:
        text (str): Input text.

    Returns:
        str: Preprocessed text.
    """
    # Remove special characters and numbers
    processed_text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Convert to lowercase
    processed_text = processed_text.lower()

    return processed_text

def preprocess_data(data):
    """
    Preprocess text data in a DataFrame.

    Args:
        data (pandas.DataFrame): DataFrame containing text data.

    Returns:
        pandas.DataFrame: DataFrame with preprocessed text data.
    """
    # Apply preprocessing function to text column
    data['preprocessed_text'] = data['text'].apply(preprocess_text)
    return data

def save_data(data, file_path):
    """
    Save data to a CSV file.

    Args:
        data (pandas.DataFrame): DataFrame containing the data to be saved.
        file_path (str): Path to save the CSV file.
    """
    data.to_csv(file_path, index=False)

def main():
    # Load data from CSV files
    train_data = load_data("../data/train_data.csv")
    valid_data = load_data("../data/valid_data.csv")

    # Preprocess data
    train_data_processed = preprocess_data(train_data)
    valid_data_processed = preprocess_data(valid_data)

    # Save preprocessed data to new CSV files
    save_data(train_data_processed, "../data/train_data_preprocessed.csv")
    save_data(valid_data_processed, "../data/valid_data_preprocessed.csv")

if __name__ == "__main__":
    main()
