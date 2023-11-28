from fastapi import APIRouter, File, UploadFile
from app.controllers.file_controller import FileController
from fastapi import Body
from fastapi.responses import FileResponse

todo_api_router = APIRouter()
file_controller = FileController()


'''
clase que maneja todas las rutas de nuestra API
'''


# ruta para el index de la api
@todo_api_router.get("/", description="Obtiene el index de la aplicación, para mostrar los gráficos")
async def get_todos():
    return FileResponse("app/templates/index.html")


@todo_api_router.get("/datasets", description="Obtiene los datasets cargados en la aplicación")
async def get_datasets():
    return file_controller.obtener_datasets()


@todo_api_router.post("/upload", description="Cargar set de datos")
async def upload_file(file: UploadFile = File(...)):
    # Process the uploaded file
    return await file_controller.upload_file(file)
