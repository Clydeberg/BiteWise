import re

class QueryParser:
    def parse(self, query:str):
        query=query.lower()

        parsed ={
            "dish":query,
            "max_price":None,
            "goal":"balanced",
            "veg_only":False,
            "people":None,
            "sort":"score"
        }
        if "veg" in query:
            parsed["veg_only"]=True

        if any(x in query for x in [
            "paneer",
            "mushroom",
            "veg salad",
            "aloo",
            "potato"
        ]):
            parsed["veg_only"]=True
        price_patterns = [
            r"(?:under|below|less than)\s*₹?\s*(\d+)",
            r"₹?\s*(\d+)"

        ]
        parsed["max_price"]=None
        for pattern in price_patterns:
            match = re.search(pattern, query)

            if match:
                value = int(match.group(1))
                parsed["max_price"]=value
            break


        people = re.search(
            r"(?:for|serve|serves)\s*(\d+)\s*(?:people|person|persons)?",
            query
        )
        if people:
            parsed["people"]=int(
                people.group(1)
            )
        else:
            parsed["people"]=1

        # price = re.search(r"(\d+)",query)

        # if price:
        #     parsed["max_price"]=int(price.group(1))
        
        if any(x in query for x in[
            "healthy",
            "health",
            "fit"
        ]):
            parsed["goal"]="healthy"

        elif any(x in query for x in[
            "protien",
            "high protien"
        ]):
            parsed["goal"]="protien"
        
        elif any(x in query for x in [
            "cheap",
            "budget",
            "low price"
        ]):
            parsed["goal"]="budget"
        
        elif any(x in query for x in [
            "low calorie",
            "low calories"
        ]):
            parsed["goal"] = "low calorie"


        remove_words=[
            "healthy",
            "health",
            "protein",
            "high protein",
            "cheap",
            "budget",
            "under",
            "below",
            "veg",
            "low calorie",
            "low calories"
        ]

        dish = query

        patterns = [
            r"(?:under|below|above|over|less than|more than)\s*₹?\s*\d+",

            r"(?:for|serve|serves)\s*\d+\s*(?:people|person|persons)?",

            r"\d+",

            r"\bhealthy\b",

            r"\bhealth\b",

            r"\bprotein\b",

            r"\bhigh protein\b",

            r"\bcheap\b",

            r"\bbudget\b",

            r"\bveg\b",

            r"\blow calorie\b",

            r"\blow calories\b"
        ]
        for pattern in patterns:
            dish=re.sub(pattern,"",dish)


        for word in remove_words:
            dish =  dish.replace(word,"")

        parsed["dish"] = " ".join(
            dish.split()
        )

        return parsed