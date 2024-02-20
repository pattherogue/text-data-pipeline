from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        str: The sentiment of the text ('positive', 'neutral', or 'negative').
    """
    # Use TextBlob to perform sentiment analysis
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Classify sentiment based on polarity score
    if sentiment > 0:
        return 'positive'
    elif sentiment == 0:
        return 'neutral'
    else:
        return 'negative'

def main():
    # Test sentiment analysis
    text = "I love this project! It's fantastic!"
    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)

if __name__ == "__main__":
    main()
