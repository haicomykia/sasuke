import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    message = 'リレーかもめ'
    return {"message": message}

if __name__ == "__main__":
    uvicorn.run("app", port=8000)