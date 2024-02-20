
                Text Data Pipeline


Description
----------------
This project implements a simple text data pipeline that preprocesses text data from CSV files, performs sentiment analysis, and provides a summary of the sentiment distribution.

File Structure
----------------
- data/
  - train_data.csv: CSV file containing training data
  - valid_data.csv: CSV file containing validation data
- src/
  - data_processing.py: Python script for data preprocessing
  - sentiment_analysis.py: Python script for sentiment analysis
  - main.py: Main Python script to execute the data pipeline

Dependencies
----------------
- Python 3.x
- pandas
- textblob

Usage
----------------
1. Place your training and validation data CSV files in the data/ directory.
2. Navigate to the src/ directory in the terminal.
3. Activate the virtual environment (if you are using one).
4. Run the main.py script using the command: python3 main.py.
5. The program will process the data, perform sentiment analysis, and provide a summary of the sentiment distribution.

Sample Output
----------------
Data processing and sentiment analysis completed successfully.
Processed 1000 records from the training data.
Processed 500 records from the validation data.
Sentiment distribution:
- Positive: 700
- Neutral: 200
- Negative: 100
