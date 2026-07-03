import requests
import json
from app.services.product_parser import normalize_products
from app.services.brand_service import BrandService

class EatSureAdapter:
    BASE_URL= (
        "https://www.eatsure.com/v1/api/search_product"
    )

    def __init__(self):
        self.brand_service = BrandService()

    def search_products(self,query:str, location: dict):
        
        # LOCATION_CONFIG = {
        #     "store_id":"10119",
        #     "city_id":"3476",
        #     "city_name":"gurgaon",
        #     "slug":"sector-23a"
        # }

        # location= {
        #     "store_id":"10119",
        #     "city_id":"3476",
        #     "city_name":"gurgaon",
        #     "slug":"sector-23a"
        # }
        cookies={
            "current_platform":"Delivery",
            "store_id": location["store_id"],
            "city_id": location["city_id"],
            "city_name": location["city_name"],
            "slug": location["slug"],
            "store_map_location": json.dumps({
                location["store_id"]:{
                    "lat":str(location["latitude"]),
                    "lng":str(location["longitude"]),
                    "place_id":"1234"
                    }
            })
        }
        # cookies={
        #     "store_id": LOCATION_CONFIG["store_id"],
        #     "city_id": LOCATION_CONFIG["city_id"],
        #     "city_name": LOCATION_CONFIG["city_name"],
        #     "slug": LOCATION_CONFIG["slug"],
        # }

        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json, text/plain, */*",
            "Referer": f"https://www.eatsure.com/{location['city_name']}/{location['slug']}"
        }
        brands = self.brand_service.get_brands(
            store_id=location["store_id"],
            city_id=location["city_id"],
            cookies=cookies,
            headers=headers
        )
        print("Brands fetched:", len(brands))
        # print(brands[:3])
        brand_lookup ={
            brand["brand_id"]: brand["brand_name"]
            for brand in brands
        }
        # print("brand_lookup")
        # print(brand_lookup)


        available_brands= ",".join(
            str(brand["brand_id"])
            for brand in brands
        )
        params={
            "keyword":query,
            "page":0,
            "availableBrands":available_brands,
            "food_type":"",
            "store_id":location["store_id"]
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
        # print("First Product brand ID:", products[0]["brand_id"])

        # print("Adapter lookup id: ",id(brand_lookup))

        return normalize_products(products, brand_lookup)
        #return normalize_products(products, brand_lookup)
    
# location= {
#             "store_id":"10119",
#             "city_id":"3476",
#             "city_name":"gurgaon",
#             "slug":"sector-23a"
#         }
# products= EatSureAdapter.search_products("paneer", location)