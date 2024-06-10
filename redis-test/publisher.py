from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis

app = FastAPI()
r = redis.Redis(host='redis', port=6379)

class Message(BaseModel):
    text: str

@app.post("/publish")
def publish_message(message: Message):
    try:
        r.publish('my_channel', message.text)
        return {"message": "Message published successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)