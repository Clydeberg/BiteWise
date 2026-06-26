class IntentExtractor:
    
    def extract(
            self,
            query
    ):
        q=query.lower()

        goal="balanced"

        if "protein" in q:
            goal = "high_protein"

        elif "healthy" in q:
            goal = "healthy"

        elif "low calorie" in q:
            goal = "low_calorie"

        elif "cheap" in q:
            goal = "budget"

        return {
            "goal": goal,
            "query": query
        }
    