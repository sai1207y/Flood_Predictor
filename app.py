import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from FloodPrediction import FloodPrediction
import pickle


app = FastAPI()
oringins =["*"]
app.add_middleware(CORSMiddleware, allow_origins=oringins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

pickle_in = open("model.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.get("/")
def index():
    return {"message": "Hello, World"}


@app.post("/predict")
def predict_flood(data: FloodPrediction):
    data = data.dict()
    rainFallMarToMay = data["rainFallMarToMay"]
    avgRainFallJun = data["avgRainFallJun"]
    avgIncreaseRainFallMayToJun = data["avgIncreaseRainFallMayToJun"]
    prediction = classifier.predict([[rainFallMarToMay, avgRainFallJun, avgIncreaseRainFallMayToJun]])
    if prediction[0] == 1:
        prediction = "Flood"
    else:
        prediction = "NO Flood"
    return {"data": prediction}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)