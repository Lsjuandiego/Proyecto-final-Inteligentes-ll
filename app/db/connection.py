from pymongo import MongoClient
import config

client = MongoClient(config.MONGO_URI)
db = client['nombre_de_tu_base_de_datos']
