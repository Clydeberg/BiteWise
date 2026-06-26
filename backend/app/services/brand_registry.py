class BrandRegistry:
    def __init__(self):
        self.brand_map={}
    
    def load(self, brands):

        self.brand_map = {
            brand["brand_id"]: brand
            for brand in brands
        }

    def get_brand(self, brand_id):

        return self.brand_map.get(
            brand_id,
            {}
        )
    
    def get_brand_name(self,brand_id):
        
        return self.brand_map.get(
            brand_id,
            {}
        ).get(
            "brand_name",
            "Unknown"
        )