# class RankingService:
#     def rank_products(self, products):
#         for product in products:
#             nutrition = product["nutrition"]

#             score=(
#                 nutrition["protein"]*3
#                 + product["rating"]*2
#                 - product["price"]/100
#             )

#             product["score"]=round(score,2)
        
#         products.sort(
#             key = lambda x:x["score"],
#             reverse=True
#         )

#         return products

class RankingService:
    def rank_products(self, products, preferences):
        goal= preferences.get("goal","balanced")
        max_price = preferences.get("max_price")
        veg_only = preferences.get("veg_only",False)

        ranked=[]

        for product in products:

            if veg_only and not product["is_veg"]:
                continue


            if (
                max_price is not None and product["price"] > max_price
            ):
                continue

            nutrition = product["nutrition"]

            protein = nutrition["protein"]
            calories = nutrition["calories"]
            fat = nutrition["fat"]

            rating = product["rating"]
            price = product["price"]


            if goal == "protein":
                score=(
                    protein*5 + rating*2 -calories*0.01 - price*0.01
                )
            elif goal=="healthy":
                score=(
                    protein*3 + rating*2 - calories*0.03 - fat*2
                )

            elif goal=="budget":
                score=(
                    rating*3 + protein -price*0.04
                )

            elif goal=="low_calorie":
                score=(
                    protein*2 + rating*2 - calories*0.05
                )
            else:
                score=(
                    protein*3 + rating*2 - price*0.01
                )

            product["score"]=round(score,2)

            ranked.append(product)

        ranked.sort(key=lambda x:x["score"],
                        reverse=True)
        return ranked
            
