from fastapi import APIRouter 
from app.schemas.search_schema import SearchRequest
from app.services.eatsure_adapter import EatSureAdapter
from app.services.product_enricher import enrich_products
from app.services.ranking_service import RankingService
from app.services.query_parser import QueryParser

router = APIRouter()

ranking_service = RankingService()

adapter = EatSureAdapter()

parser = QueryParser()


@router.post("/search")
def search_products(request: SearchRequest):
    print(
        parser.parse(
            request.query
        )
    )
    location= {
            "latitude": 28.497093258176825,
            "longitude": 77.06125050387696,
            "store_id":"10119",
            "city_id":"3476",
            "city_name":"gurgaon",
            "slug":"sector-23a"
        }
    preferences = parser.parse(request.query)

    products = adapter.search_products(
        # query=request.query, 
        preferences["dish"],
        location=location
    )
    # products = enrich_products(products)

    # products = ranking_service.rank_products(products)


    if isinstance(products, dict) and products.get("error"):
        return products
    
    products=enrich_products(products)
    # print("After enrich:")
    # print(products[0])
    print(preferences)
    products=ranking_service.rank_products(products, preferences)


    return{
        "success":True,
        "count":len(products),
        "products": products
    }