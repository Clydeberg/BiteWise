from fastapi import APIRouter 
from app.schemas.search_schema import SearchRequest
from app.services.eatsure_adapter import EatSureAdapter
from app.services.product_enricher import enrich_products
from app.services.ranking_service import RankingService

router = APIRouter()

ranking_service = RankingService()

adapter = EatSureAdapter()

@router.post("/search")
def search_products(request: SearchRequest):
    products = adapter.search_products(
        request.query
    )
    products = enrich_products(products)

    products = ranking_service.rank_products(products)

    return{
        "success":True,
        "products": products
    }