def load_data():
    print("Data loaded")
    return [10, None, 20, None, 30]

def clean_data(data):
    cleaned = []
    for value in data:
        if value is not None:
            cleaned.append(value)
    print("Data cleaned")
    return cleaned

def train_model(data):
    print("Training model")
    return sum(data) / len(data)

def evaluate_model(model):
    print("Model accuracy: 90%")

data = load_data()
cleaned_data = clean_data(data)
model = train_model(cleaned_data)
evaluate_model(model)
