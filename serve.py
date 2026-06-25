import http.server, socketserver, functools

DIRECTORY = "/Users/work/Documents/Claude Code Projects/Adore Life/site"
PORT = 4178

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
