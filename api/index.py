from http.server import BaseHTTPRequestHandler

tata = 'test-rando'
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        text = f'hola {tata}'
        self.wfile.write(text.encode('utf-8'))
        return
