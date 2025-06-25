from http.server import HTTPServer, SimpleHTTPRequestHandler

port = 8080

server_address = ("", port)

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"Server started in port:{port}")
httpd.serve_forever()
