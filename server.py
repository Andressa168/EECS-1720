import http.server
import socketserver

PORT = 9090 #3030, 8887, 8898, 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
  print("Hi you are at PORT: ", PORT)
  httpd.serve_forever()


# to run>: python3 server.py
# might have to install the imports
# pip/pip3 install http.server, socketserver
# 
