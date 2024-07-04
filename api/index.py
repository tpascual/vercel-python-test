from http.server import BaseHTTPRequestHandler
import os
from pymongo import MongoClient

# Obtener la cadena de conexión desde la variable de entorno
#uri = os.getenv("MONGODB_URI")
uri = os.environ.get('MONGODB_URI')

if uri is None:
    raise ValueError("No se encontró la variable de entorno MONGODB_URI")

# Conectarse al cliente de MongoDB
client = MongoClient(uri)

# Seleccionar la base de datos y la colección
db = client.testDante
collection = db.helloCollection

# Crear el documento a insertar
document = {
    "message": "Hello"
}

# Insertar el documento en la colección
result = collection.insert_one(document)

# Confirmar que el documento ha sido insertado
print(f"Inserted document with id: {result.inserted_id}")

tata = os.environ.get('PPP')
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        text = f'hola {tata}'
        self.wfile.write(text.encode('utf-8'))
        return
