from pydantic import BaseModel
from datetime import datetime
class CleanRequest(BaseModel):
    url:str
class CleanResponse(BaseModel):
    original_url:str
    cleaned_url:str
    timestamp:datetime