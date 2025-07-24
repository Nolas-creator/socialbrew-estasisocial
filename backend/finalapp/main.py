from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.posts import post_router
from routes.auth import auth_router
from routes.uploads import upload_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",              # desarrollo local
        "https://socialbrew.onrender.com"     # frontend en producción
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router)
app.include_router(auth_router)
app.include_router(upload_router)

@app.get("/")
def root():
    return {"message": "SocialBrew API 🚀"}
