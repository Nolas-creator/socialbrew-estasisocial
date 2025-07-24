from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta
from passlib.context import CryptContext
from pydantic import BaseModel

auth_router = APIRouter()
SECRET_KEY = "secreto_socialbrew"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$X.ePns3ZJ0rkBrfLVoJ2Qej7IHjKGVIF1a46omKvA/3VPMdTxoQvy"  # 1234
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

@auth_router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict or not pwd_context.verify(form_data.password, user_dict["hashed_password"]):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    access_token = jwt.encode(
        {"sub": user_dict["username"], "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)},
        SECRET_KEY, algorithm=ALGORITHM
    )
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.get("/protected")
async def protected(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": f"Hola {payload.get('sub')}, estás autenticado!"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")