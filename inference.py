import joblib

model = None


def load_model(path="iris_model.joblib"):
    global model
    model = joblib.load(path)


def predict(input_data):
    return ["setosa", "versicolor", "virginica"][model.predict([input_data])[0]]
