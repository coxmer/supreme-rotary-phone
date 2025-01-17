from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('FamilyWsb/chat.html', 'rb') as file:
            self.wfile.write(file.read())
        with open('FamilyWsb/script.js', 'rb') as file:
            self.wfile.write(b'<script src="script.js"></script>')
        with open('FamilyWsb/styles.css', 'rb') as file:
            self.wfile.write(b'<style>')
            self.wfile.write(file.read())
            self.wfile.write(b'</style>')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        print("received data: ", data)
        if 'message' in data and data['message']:
            print("received message: ", data['message'])
            with open('message.txt', 'a') as file:
                file.write(data['message'] + '\n')
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({'status': 'success', "data": data})
        self.wfile.write(response.encode('utf-8'))

    def do_POST_message(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        print("received data: ", data)
        if 'message' in data and data['message']:
            print("received message: ", data['message'])
            with open('message.txt', 'a') as file:
                file.write(data['message'] + '\n')
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({'status': 'success', "data": data})
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        if self.path == '/message':
            self.do_POST_message()
        else:
            pass

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('192.168.0.106', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {server_address}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()