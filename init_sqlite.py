import sqlite3
import os
import bcrypt

#Ruta de la base de datos SQLite
db_path = './data/users.db'

#crea la carpeta data si no existe
os.makedirs('./data', exist_ok=True)

#Conexión a la base de datos SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear la tabla de usuarios si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
    )
''')


init_users = [
    ('admin', '1111'),
    ('Ale', '1234'),
    ('user1', '1234'),
    ('user2', '1234'),
]

#Insertar usuarios iniciales si no existen
for username, password in init_users:
    #tipo de datos byte para almacenar la contraseña
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password)
        VALUES (?, ?)
    ''', (username, hashed_password.decode('utf-8')))

# Guardar los cambios
conn.commit()
# Cerrar la conexión a la base de datos
conn.close()
    
print("base de datos creada correctamente.")
print("Usuario insertado correctamente.")