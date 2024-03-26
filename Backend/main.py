from fastapi import FastAPI
from routes.route import router
from routes.auth import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)
app.include_router(auth)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Altere para o URL do seu aplicativo React
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"]
)