from fastapi import APIRouter, Query

router = APIRouter()

# Example in-memory dataset (you can replace this with database logic later)
properties_data = [
    {"id": 1, "address": "123 Main St", "city": "Flint", "state": "MI"},
    {"id": 2, "address": "456 Oak Ave", "city": "Burton", "state": "MI"},
    {"id": 3, "address": "789 Pine Rd", "city": "Grand Blanc", "state": "MI"},
]

@router.get("/search")
def search_properties(query: str = Query(..., min_length=1)):
    """
    Simple search endpoint that filters properties by address or city.
    Replace this with your database search later.
    """
    query_lower = query.lower()
    results = [
        p for p in properties_data
        if query_lower in p["address"].lower() or query_lower in p["city"].lower()
    ]
    return results
@router.get("/")
def list_properties():
    return properties_data
from pydantic import BaseModel

class PropertyCreate(BaseModel):
    address: str
    city: str
    state: str

@router.post("/")
def create_property(new_property: PropertyCreate):
    """
    Create a new property and add it to the in-memory list.
    Later, you'll replace this with a database insert.
    """
    new_id = len(properties_data) + 1
    property_dict = {
        "id": new_id,
        "address": new_property.address,
        "city": new_property.city,
        "state": new_property.state,
    }
    properties_data.append(property_dict)
    return property_dict
from pydantic import BaseModel

class PropertyUpdate(BaseModel):
    address: str | None = None
    city: str | None = None
    state: str | None = None

@router.put("/{property_id}")
def update_property(property_id: int, updates: PropertyUpdate):
    """
    Update an existing property by ID.
    Only fields provided will be updated.
    """
    for p in properties_data:
        if p["id"] == property_id:
            if updates.address is not None:
                p["address"] = updates.address
            if updates.city is not None:
                p["city"] = updates.city
            if updates.state is not None:
                p["state"] = updates.state
            return p

    return {"error": "Property not found"}
@router.post("/")
def create_property(new_property: PropertyCreate):
    ...
    return property_dict

@router.put("/{property_id}")
def update_property(property_id: int, updates: PropertyUpdate):
    ...
from pydantic import BaseModel, Field

class PropertyCreate(BaseModel):
    address: str = Field(..., min_length=3, max_length=100)
    city: str = Field(..., min_length=2, max_length=50)
    state: str = Field(..., min_length=2, max_length=2, pattern="^[A-Z]{2}$")

class PropertyUpdate(BaseModel):
    address: str | None = Field(None, min_length=3, max_length=100)
    city: str | None = Field(None, min_length=2, max_length=50)
    state: str | None = Field(None, min_length=2, max_length=2, pattern="^[A-Z]{2}$")
@router.delete("/properties/{property_id}")
def delete_property(property_id: int):
    for index, prop in enumerate(properties):
        if prop["id"] == property_id:
            del properties[index]
            return {"message": "Property deleted"}
    return {"error": "Property not found"}

