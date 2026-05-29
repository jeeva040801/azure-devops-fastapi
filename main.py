from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "API is running perfectly!"}

@app.get("/query/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "data": "Sample retrieved context"}
