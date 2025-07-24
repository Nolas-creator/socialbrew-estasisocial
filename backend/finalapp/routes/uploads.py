from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from uuid import uuid4

upload_router = APIRouter()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_CONTENT_TYPES = {
    "image/jpeg", "image/png", "image/gif",
    "video/mp4", "video/webm", "video/ogg"
}
MAX_FILE_SIZE = 50 * 1024 * 1024

@upload_router.post("/files/upload/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido.")
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Archivo demasiado grande.")
    filename = f"{uuid4().hex}{Path(file.filename).suffix}"
    path = UPLOAD_DIR / filename
    with open(path, "wb") as f:
        f.write(contents)
    return {"filename": filename, "url": f"http://localhost:8000/files/{filename}"}

@upload_router.get("/files/{filename}")
async def get_file(filename: str):
    path = UPLOAD_DIR / filename
    if not path.exists():
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    return FileResponse(path)