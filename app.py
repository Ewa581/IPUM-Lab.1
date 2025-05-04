from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict

app = FastAPI()
load_model()  # Ładuje model przy starcie


@app.post("/predict", response_model=PredictResponse)
def predict_iris(request: PredictRequest):
    input_data = [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    ]
    return PredictResponse(prediction=predict(input_data))
