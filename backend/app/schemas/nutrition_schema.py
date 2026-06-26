from pydantic import BaseModel

class NutritionInfo(BaseModel):
    calories: float
    protein: float
    carbs: float
    fat:float
