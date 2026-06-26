from app.schemas.nutrition_schema import NutritionInfo

class NutritionService:
    def get_nutrition(self,dish_name:str):
        dish=dish_name.lower()

        if "chicken" in dish:
            return{
                "calories": 720,
                "protein": 28,
                "carbs": 82,
                "fat": 22
            }
        if "paneer" in dish:
            return{
                "calories": 650,
                "protein": 22,
                "carbs": 70,
                "fat": 24
            }
        
        return{
            "calories": 500,
            "protein": 15,
            "carbs": 60,
            "fat": 15
            }
