def calculate_accuracy(predictions, targets):
    correct = sum(p == t for p, t in zip(predictions, targets))
    total = len(predictions)
    accuracy = correct / total
    return accuracy

def calculate_precision(predictions, targets):
    true_positives = sum(p == 1 and t == 1 for p, t in zip(predictions, targets))
    predicted_positives = sum(p == 1 for p in predictions)
    precision = true_positives / predicted_positives if predicted_positives > 0 else 0
    return precision

def calculate_recall(predictions, targets):
    true_positives = sum(p == 1 and t == 1 for p, t in zip(predictions, targets))
    actual_positives = sum(t == 1 for t in targets)
    recall = true_positives / actual_positives if actual_positives > 0 else 0
    return recall

def calculate_f1_score(predictions, targets):
    precision = calculate_precision(predictions, targets)
    recall = calculate_recall(predictions, targets)
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return f1_score
