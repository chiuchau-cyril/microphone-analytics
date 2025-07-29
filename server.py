#!/usr/bin/env python3
"""
簡單的 HTTP 伺服器，用於解決 CORS 問題
使用方法：python3 server.py
然後在瀏覽器中打開 http://localhost:8000
"""

import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"伺服器運行在 http://localhost:{PORT}")
    print("按 Ctrl+C 停止伺服器")
    httpd.serve_forever()