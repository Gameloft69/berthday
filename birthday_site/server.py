#!/usr/bin/env python3
import os
import http.server
import socketserver

os.chdir('/c/Users/karpo/Desktop/birthday_site')
PORT = 8080
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', PORT), handler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    httpd.serve_forever()
