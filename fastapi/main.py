from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    name = "Yosef"
    return {f"Hello, {name}"}

@app.get("/{name}")
async def read_item(name: str):
    return {"message": f"Hello, {name}"}