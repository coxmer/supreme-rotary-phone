'''
在代码"def do_GET(self)"中，“###”从上至下为"chat.html","script.js","styles.css"，使用时请加上相对路径，如"animals/chat.html".
'''
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('###', 'rb') as file:
            self.wfile.write(file.read())
        with open('###', 'rb') as file:
            self.wfile.write(b'<script src="script.js"></script>')
        with open('###', 'rb') as file:
            self.wfile.write(b'<style>')
            self.wfile.write(file.read())
            self.wfile.write(b'</style>')

    def do_POST(self):
        if self.path == '/message':
            self.handle_message()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_message(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        # Check if the message is present
        if 'message' in data and data['message']:
            print("Received message: ", data['message'])
            # Save the message to a file
            with open('messages.txt', 'a') as file:
                file.write(data['message'] + '\n')
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({'status': 'success', 'data': data})
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)  # Listen on all interfaces
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
