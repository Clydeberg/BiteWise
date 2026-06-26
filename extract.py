import json

with open("resp.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

results = []

def find_brands(obj):
    if isinstance(obj, dict):
        if all(k in obj for k in ["brand_id","brand_name","slug","main_offering"]):
            results.append({
                "brand_id": obj["brand_id"],
                "brand_name": obj["brand_name"],
                "slug": obj["slug"],
                "main_offering": obj["main_offering"]
            })

        for value in obj.values():
            find_brands(value)

    elif isinstance(obj, list):
        for item in obj:
            find_brands(item)


find_brands(data)

print(results)