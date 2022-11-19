from fastapi import FastAPI

app = FastAPI()


@app.get("/predicate")
async def hello():
    return {"message": "hello world!"}