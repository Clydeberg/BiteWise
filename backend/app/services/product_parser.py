def normalize_products(products):

    normalized=[]

    for item in products:{
        normalized.append({
            # "product_id":item["product_id"],
            # "name": item["product_name"],
            # "price": item["price"],
            # "rating": item["rating"],
            
            # "image_url": item["image"],
            # "is_veg": bool(item["is_veg"])
            "product_id":item["product_id"],

            "name":item["product_name"],

            "brand_id":item["brand_id"],

            "price":item["price"],

            "rating":item["rating"],

            "image_url":item["image"],

            "is_veg":bool(
                    item["is_veg"]
                )

        })
    }
    return normalized