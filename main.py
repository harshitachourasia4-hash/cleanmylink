from fastapi import FastAPI,HTTPException
from models import CleanRequest,CleanResponse
from datetime import datetime,timezone
from cleaner import clean_url
app=FastAPI(title="URL Cleaner API",
            description="Strips UTM and tracking params")
@app.post("/clean",response_model=CleanResponse)
def clean_my_url(req:CleanRequest):
    if not req.url.startswith(("http://","https://")):
        raise HTTPException(status_code=422,detail="url must be started with https:// ,https://")
    return CleanResponse(
        original_url=req.url,
        cleaned_url=clean_url(req.url),
    timestamp=datetime.now(timezone.utc)
    )