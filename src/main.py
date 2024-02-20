# main.py

# Import necessary modules
from src.data_processing import load_data, preprocess_data, save_data
from src.model_training import train_model
from src.evaluation import evaluate_model

def main():
    # Load data
    train_data = load_data("data/train_data.csv")
    valid_data = load_data("data/valid_data.csv")

    # Preprocess data
    train_data_processed = preprocess_data(train_data)
    valid_data_processed = preprocess_data(valid_data)

    # Save preprocessed data
    save_data(train_data_processed, "data/train_data_preprocessed.csv")
    save_data(valid_data_processed, "data/valid_data_preprocessed.csv")

    # Train model
    model = train_model(train_data_processed)

    # Evaluate model
    evaluation_results = evaluate_model(model, valid_data_processed)

    # Print evaluation results
    print("Evaluation Results:")
    print(evaluation_results)

if __name__ == "__main__":
    main()
