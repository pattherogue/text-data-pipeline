from data_processing import load_data, preprocess_data, save_data
from sentiment_analysis import analyze_sentiment

def main():
    # Load data from CSV files
    train_data = load_data("../data/train_data.csv")
    valid_data = load_data("../data/valid_data.csv")

    # Preprocess data
    train_data_processed = preprocess_data(train_data)
    valid_data_processed = preprocess_data(valid_data)

    # Apply sentiment analysis to preprocessed text
    train_data_processed['sentiment'] = train_data_processed['preprocessed_text'].apply(analyze_sentiment)
    valid_data_processed['sentiment'] = valid_data_processed['preprocessed_text'].apply(analyze_sentiment)

    # Save preprocessed data with sentiment labels to new CSV files
    save_data(train_data_processed, "../data/train_data_preprocessed.csv")
    save_data(valid_data_processed, "../data/valid_data_preprocessed.csv")

    # Print out summary information
    print("Data processing and sentiment analysis completed successfully.")
    print("Processed {} records from the training data.".format(len(train_data_processed)))
    print("Processed {} records from the validation data.".format(len(valid_data_processed)))

    # Calculate sentiment distribution
    sentiment_distribution_train = train_data_processed['sentiment'].value_counts()
    sentiment_distribution_valid = valid_data_processed['sentiment'].value_counts()

    print("Sentiment distribution:")
    print("- Positive:", sentiment_distribution_train.get('positive', 0))
    print("- Neutral:", sentiment_distribution_train.get('neutral', 0))
    print("- Negative:", sentiment_distribution_train.get('negative', 0))

if __name__ == "__main__":
    main()
