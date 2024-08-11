from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth_router, user_router, taxi_router, client_router

app = FastAPI()

origins = [
    "http://localhost:3000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(taxi_router.router)
app.include_router(client_router.router)
