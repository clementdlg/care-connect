from fastapi import FastAPI
from routes.administrator_routes import router as administrator_router
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

app.include_router(administrator_router, prefix="/administrator")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
