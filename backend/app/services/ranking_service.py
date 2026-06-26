class RankingService:
    def rank_products(self, products):
        for product in products:
            nutrition = product["nutrition"]

            score=(
                nutrition["protein"]*3
                + product["rating"]*2
                - product["price"]/100
            )

            product["score"]=round(score,2)
        
        products.sort(
            key = lambda x:x["score"],
            reverse=True
        )

        return products