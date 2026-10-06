from fastapi import FastAPI
from app.routers.properties import router as properties_router

app = FastAPI()

app.include_router(properties_router, prefix="/properties", tags=["properties"])

@app.get("/")
def root():
    return {"message": "Genesee CRM API is running"}
