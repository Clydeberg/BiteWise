from fastapi import FastAPI
from app.api.search import router

app=FastAPI(
    title= "BiteWise AI"
)

app.include_router(router)