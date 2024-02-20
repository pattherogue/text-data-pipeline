import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    preprocessed_text = ' '.join(filtered_tokens)
    return preprocessed_text

def preprocess_data(data):
    data['preprocessed_text'] = data['text'].apply(preprocess_text)
    return data

def main():
    train_data = load_data("../data/train_data.csv")
    valid_data = load_data("../data/valid_data.csv")

    train_data_processed = preprocess_data(train_data)
    valid_data_processed = preprocess_data(valid_data)

    train_data_processed.to_csv("../data/train_data_preprocessed.csv", index=False)
    valid_data_processed.to_csv("../data/valid_data_preprocessed.csv", index=False)

if __name__ == "__main__":
    main()
