import requests

class BrandService:
    BASE_URL=(
        "https://www.eatsure.com/v1/api/get_all_brands"
    )

    def get_brands(
            self,
            store_id,
            city_id,
            cookies
    ):
        response = requests.get(
            self.BASE_URL,
            params={
                "store_id": store_id,
                "city_id":city_id
            },
            cookies=cookies
        )

        response.raise_for_status()
        brands = response.json()["data"]["data"]

        normalized=[]

        for brand in brands:
            normalized.append({
                "brand_id": brand["brand_id"],

                "brand_name": brand["brand_name"],

                "slug": brand["slug"],

                "main_offering": brand["main_offering"]
            })
        return normalized