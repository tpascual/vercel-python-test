from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Obtener la fecha de inserción usando la función local
        
        # Usar una f-string para incluir el valor de la variable
        response_text = f'Hello, world! {insertion_date}'
        self.wfile.write(response_text.encode('utf-8'))
        return
