from fastapi import APIRouter, File, UploadFile
from app.controllers.file_controller import FileController
from fastapi import Body
from fastapi.responses import FileResponse

todo_api_router = APIRouter()
file_controller = FileController()


'''
clase que maneja todas las rutas de nuestra API
'''


@todo_api_router.post("/upload", description="Cargar set de datos")
async def upload_file(file: UploadFile = File(...)):
    # Process the uploaded file
    return await file_controller.upload_file(file)
