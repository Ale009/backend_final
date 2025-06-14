from flask import Blueprint, request, jsonify, current_app
import json, base64
import bcrypt
from db_sqlite import query_db, insert_db

auth_bp = Blueprint('auth', __name__)

def load_db():
    with open(current_app.config['DATABASE_PHOTO']) as f:
        return json.load(f)
    
def save_db(data):
    with open(current_app.config['DATABASE_PHOTO'], 'w') as f:
        json.dump(data, f, indent=2)
        
@auth_bp.route('/login', methods=["POST"])
def login():
    data = request.json # Datos que vienen de postman (cliente)
    #db = load_db() # Datos que estan en el servidor (DB)
    user = query_db(
        'SELECT * FROM users WHERE username = ?',
        (data['username'], ), one=True
    )
    if user:
        stored_hash = user['password']
        #Contraseña proporcionada por el usuario y el hash_bytes almacenado en la base de datos
        password_bytes = data['password'].encode('utf-8')
        stored_hash_bytes = stored_hash.encode('utf-8')
        # Verifica si la contraseña proporcionada coincide con el hash almacenado
        if bcrypt.checkpw(password_bytes, stored_hash_bytes):
            return jsonify({ 'mensaje': 'Login exitoso', 'user_id': user["id"] }), 200  

    return jsonify({ 'error': 'Credenciales inválidas' }), 401

# Ruta para registrar un nuevo usuario
@auth_bp.route('/register', methods=["POST"])
def register():
    #data = request.json
    file = request.files['photo']
    username = request.form.get('username')
    password = request.form.get('password')    
    # Verificar si el usuario ya existe
    existing_user = query_db(
        'SELECT username FROM users WHERE username = ?',
        ('username', ), one=True
    )
    if existing_user:
        return jsonify({ 'error': 'Usuario ya existe' }), 400
    
    # Hashear la contraseña antes de guardarla
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    #insterar el nuevo usuario en la base de datos
    user_id = insert_db(
        'INSERT INTO users (username, password) VALUES (?, ?)',
        (username, hashed_password)
    )
    
    if file:
        file_data = file.read() #leyendo el contenido del archivo como binario
        encoded_data = base64.b64encode(file_data).decode('utf-8') #codificando la imagen en base64
    
        db = load_db()
        new_photo = {
            "id": len(db["photos"]) + 1,
            "user_id": user_id,
            "filename": file.filename,
            "filedata": encoded_data
        }
        db["photos"].append(new_photo)
        save_db(db)
        return jsonify({"message": "Foto agregada"}), 201

    return jsonify({ 'message': 'Registrado correctamente' }), 200



    #user = db["users"].append({
    
    # Si existe un username en base de datos que sea igual al que viene en el request
    #if any(u["username"] == data["username"] for u in ["users"]):
    #   return jsonify({ 'error': 'Usuario ya existe' }), 400

    #newUser = {
    #    'id': len(db['users']) + 1, # 3
    #    'username': data['username'],
    #    'password': data['password']
    
    #db["users"].append(newUser)
    #save_db(db)

@auth_bp.route('/users', methods=["GET"])
def get_users():
    users = query_db("SELECT id, username FROM users")
    return jsonify([dict(user) for user in users]), 200