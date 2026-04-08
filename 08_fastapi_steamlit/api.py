from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"message":"HEllO world"}

@app.get("/items")
async def get_items():
    return [{
        "name":"Home"
    },
    {
        "name":"ItemList"
    }]