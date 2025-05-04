from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib


def load_data():
    return load_iris(return_X_y=True)


def train_model():
    X, y = load_data()
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model


def save_model(model, path="iris_model.joblib"):
    joblib.dump(model, path)


if __name__ == "__main__":
    model = train_model()
    save_model(model)
