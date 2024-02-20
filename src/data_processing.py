import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

nltk.download('stopwords')
nltk.download('punkt')

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
    Preprocess text data by removing stopwords and special characters.

    Args:
        text (str): Input text.

    Returns:
        str: Preprocessed text.
    """
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Join tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text

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
