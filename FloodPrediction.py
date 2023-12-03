from pydantic import BaseModel
class FloodPrediction(BaseModel):
    rainFallMarToMay: float
    avgRainFallJun: float
    avgRainFallJul: float
    avgIncreaseRainFallMayToJun: float