from app.services.nutrition_service import NutritionService
from app.services.brand_registry import BrandRegistry


nutrition_service = NutritionService()

def enrich_products(products, brand_registry):
    enriched = []

    for product in products:
        enriched_product = product.copy()
        enriched_product["brand_name"] = (
            brand_registry.get_brand_name(product.get("brand_id"))
        )
        nutrition = nutrition_service.get_nutrition(
            product["name"]
        )
        enriched_product["nutrition"] = nutrition_service.get_nutrition(product.get("name"))
        enriched.append(enriched_product)
    return enriched