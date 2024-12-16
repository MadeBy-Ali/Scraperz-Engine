from pydantic import BaseModel, ValidationError

class ProductSchema(BaseModel):
    name: str
    price: str
    url: str
    
def validate_data(data):
    try:
        return ProductSchema(**data).model_dump()
    except ValidationError as e:
        print("Data invalid:{e}")
        return None