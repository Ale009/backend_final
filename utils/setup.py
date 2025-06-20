import os
from config import Config
import json

def init_directories():
    os.makedirs(Config.DATA_FOLDER, exist_ok=True)

def init_database():
    if not os.path.exists(Config.DATABASE_FILE):
        with open(Config.DATABASE_FILE, 'w') as f:
            json.dumps({ "users": [] }, f) # Contenido de la base de datos JSON al inicio
    if not os.path.exists(Config.DATABASE_PHOTO):
        with open(Config.DATABASE_PHOTO, 'w') as f:
            json.dumps({ "photos": [] }, f) # Contenido de la base de datos JSON al inicio
            