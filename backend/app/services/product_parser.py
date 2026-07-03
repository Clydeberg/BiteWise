def normalize_products(products, brand_lookup):
    # print("Parser lookup id: ", id(brand_lookup))

    normalized=[]

    for item in products:
        # print("=" * 60)
        # print("Current brand_id:", item["brand_id"], type(item["brand_id"]))
        # print("Lookup result:", brand_lookup.get(item["brand_id"]))
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

            "brand_name": brand_lookup.get(item["brand_id"],"Unknown"),

            "price":item["price"],

            "rating":item["rating"],

            "image_url":item["image"],

            "is_veg":bool(
                    item["is_veg"]
                )

        })
    return normalized