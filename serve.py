import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map[".m3u8"]="vnd.apple.mpegURL"
Handler.extensions_map[".ts"]="video/MP2T"
Handler.extensions_map[".mp4"]="video/mp4"


httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()