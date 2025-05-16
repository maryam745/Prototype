from fastapi import FastAPI

app = FastAPI()

@app.get("/search{num}")
async def read_root(num:int):
    return {"message": f"{num+num}"}

@app.get("/")
async def read_root():
    return {"message": "home"}
