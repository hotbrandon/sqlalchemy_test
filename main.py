from fastapi import FastAPI
import uvicorn
from routes import sqldemo, user

app = FastAPI()


@app.get("/")
async def index():
    return {"hello"}

app.include_router(
    router=user.router,
    prefix="/users",
    tags=["user"]
)

app.include_router(
    router=sqldemo.router,
    prefix="/sqldemo",
    tags=["sqlalchemy demo"]
)

if __name__ == "__main__":
    uvicorn.run(app)
