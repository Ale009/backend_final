# BACKEND - PROYECTO FINAL

Este proyecto fue desarrollado en **PYTHON**, implementando interacción con el `FRONTEND` mediante `FLASK`. A continuación, se detallan los módulos trabajados:

## 🚀 Módulos Implementados

### 1. **LOGIN**  
   - **Descripción**:  
     Página de autenticación donde el usuario ingresa sus credenciales (usuario y contraseña) para acceder al contenido.  
   - **Validaciones**:  
     - Las credenciales se encriptan por medio de la librería `bcrypt`.  
     - El almacenamiento se realiza para las credenciales en la base de datos SQLite.  

### 2. **REGISTRO**  
   - **Descripción**:
       Al momento que el usuario crea su cuenta se realizan los siguientes procesos:
     - Nombre de usuario y contraseña (encriptada por medio de `bcrypt`) se almacenan en la base de datos SQLite.  
     - La fotografía de perfil se almacena en un archivo de typo `JSON`, esta se codifica en `base64`.

### 3. **ÍNDICE (Galería)**  
   - **Descripción**:  
     Para mostrar el feed con todas las imágenes subidas por los usuarios, se realiza:  
     - Al agregar fotos el usuario se almacenan las imagenes en un archivo typo `JSON`, esta se codifica en `base64`.
     - La sección de comentarios en cada imagen se almacena también en el mismo archivo json para mantener el vínculo.
