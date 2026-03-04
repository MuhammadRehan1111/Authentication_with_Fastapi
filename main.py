from fastapi import FastAPI
from app.routers import user,analysis

app = FastAPI()

app.include_router(user.router,prefix="/user",tags=["User"])
app.include_router(analysis.router,prefix="/analisis",tags=["Analysis"])

@app.get("/")
def root():
    return{"message":" api is running securely"}
