import sqlite3
from flask import g
from config import Config

DATABASE = Config.SQLITE_DB

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

# Método para  consultar si existe algo en la bd
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Método para modificar la base de datos
def modify_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    cur.close()

#Método para insert datos en la base de datos
def insert_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    last_id = cur.lastrowid
    cur.close()
    return last_id

# Método para cerrar la conexión a la base de datos
def close_connection(e=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        g._database = None
        
    
