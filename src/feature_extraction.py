from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def extract_tfidf_features(preprocessed_texts):
    """
    Extract TF-IDF features from preprocessed text data.

    Args:
        preprocessed_texts (list): List of preprocessed text data.

    Returns:
        tuple: Tuple containing the trained TfidfVectorizer and TF-IDF features.
    """
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_features = tfidf_vectorizer.fit_transform(preprocessed_texts)
    return tfidf_vectorizer, tfidf_features

def save_tfidf_features(tfidf_features, filename):
    """
    Save TF-IDF features to a file.

    Args:
        tfidf_features: TF-IDF features to be saved.
        filename (str): Name of the file to save the features.
    """
    joblib.dump(tfidf_features, filename)

if __name__ == "__main__":
    # Example usage:
    preprocessed_texts = ["preprocessed text 1", "preprocessed text 2", ...]  # Replace with your preprocessed texts
    tfidf_vectorizer, tfidf_features = extract_tfidf_features(preprocessed_texts)
    save_tfidf_features(tfidf_features, 'tfidf_features.pkl')
