import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def remove_html_tags(text):
    clean_text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove special characters
    return clean_text

def tokenize_text(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token.lower() not in stop_words]

def stem_tokens(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

def preprocess_text(text):
    cleaned_text = remove_html_tags(text)
    tokens = tokenize_text(cleaned_text)
    tokens = remove_stopwords(tokens)
    # Uncomment one of the following lines to choose between stemming or lemmatization
    # tokens = stem_tokens(tokens)
    # tokens = lemmatize_tokens(tokens)
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

if __name__ == "__main__":
    # Example usage:
    text = "This is <b>example</b> text with HTML tags and special characters. It needs to be preprocessed."
    preprocessed_text = preprocess_text(text)
    print("Preprocessed text:")
    print(preprocessed_text)
