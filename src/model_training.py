from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

def train_model(train_data, valid_data):
    # Build a pipeline for text classification
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])

    # Fit the model
    X_train = train_data['preprocessed_text']
    y_train = train_data['label']
    pipeline.fit(X_train, y_train)

    return pipeline

def evaluate_model(model, valid_data):
    X_valid = valid_data['preprocessed_text']
    y_valid = valid_data['label']
    predictions = model.predict(X_valid)

    # Calculate evaluation metrics
    accuracy = calculate_accuracy(predictions, y_valid)
    precision = calculate_precision(predictions, y_valid)
    recall = calculate_recall(predictions, y_valid)
    f1_score = calculate_f1_score(predictions, y_valid)

    return accuracy, precision, recall, f1_score
