from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="CSV Analytics Dashboard",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "CSV Analytics Dashboard API Running"
    }