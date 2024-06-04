from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def read_item(name: str):
    return {"message": f"Hello, {name}"}