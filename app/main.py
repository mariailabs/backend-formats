from fastapi import FastAPI
from routers import auth_router, user_router 

app = FastAPI()
app.include_router(auth_router.router)
app.include_router(user_router.router)





