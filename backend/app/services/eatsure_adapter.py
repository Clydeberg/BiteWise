import requests
from app.services.product_parser import normalize_products

class EatSureAdapter:
    BASE_URL= (
        "https://www.eatsure.com/v1/api/search_product"
    )

    def search_products(self,query:str):
        LOCATION_CONFIG = {
            "store_id":"10119",
            "city_id":"3476",
            "city_name":"gurgaon",
            "slug":"sector-23a"
        }
        params={
            "keyword":query,
            "page":0,
            "availableBrands":"21,26,25,30,218,175,241",
            "food_type":"",
            "store_id":"10119"
        }
        cookies={
            "store_id": LOCATION_CONFIG["store_id"],
            "city_id": LOCATION_CONFIG["city_id"],
            "city_name": LOCATION_CONFIG["city_name"],
            "slug": LOCATION_CONFIG["slug"],
        }

        headers={
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=20
        )

        print("STATUS:", response.status_code)
        if response.status_code !=200:
            return{
                "error":True,
                "status_code":response.status_code,
                "response":response.text
            }
        #print("RESPONSE:", response.text)
        # print(response.url)
        # print(response.json().keys())

        # products = response.json()["data"]["products"]
        # print(products[0])
        # # print(products[1])
        # # print(products[2])

        # return response.json()

        data=response.json()

        products= data["data"]["products"]

        return normalize_products(products)