class BrandRecommender:

    def recommend(self,goal,brands):
        recommendations=[]
        for brand in brands:
            offering = (
                brand["main_offering"].lower()
            )
            if(
                goal=="high_protien" 
                and (
                    "wrap" in offering or "bowl in offering"
                )
            ):
                recommendations.append(brand)
            elif (
                goal == "pizza"
                and
                "pizza"
                in offering
            ):
                recommendations.append(
                    brand
                )

            elif (
                goal == "dessert"
                and
                "dessert"
                in offering
            ):
                recommendations.append(
                    brand
                )

            return recommendations
        