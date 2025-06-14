import os

class Config:
    DATA_FOLDER = './data'
    DATABASE_FILE = os.path.join(DATA_FOLDER, 'database.json') # ./data/database.json
    DATABASE_PHOTO = os.path.join(DATA_FOLDER, 'dataphoto.json')
    SQLITE_DB = os.path.join(DATA_FOLDER, 'users.db') # ./data/users.db