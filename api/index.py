from http.server import BaseHTTPRequestHandler
import os
from pymongo.mongo_client import MongoClient

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Obtener la cadena de conexión desde la variable de entorno
        uri = os.environ.get('MONGODB_URI')

        if uri is None:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Variable de entorno MONGODB_URI no encontrada'.encode('utf-8'))
            return

        try:
            # Conectarse al cliente de MongoDB
            client = MongoClient(uri)
            client.admin.command('ping')
            # Verificar la conexión listando las bases de datos
            #client.list_database_names()
            # Si la conexión es exitosa, responder con "OK"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('OK'.encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Error al conectar con MongoDB: {str(e)}'.encode('utf-8'))

