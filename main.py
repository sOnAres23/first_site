from http.server import BaseHTTPRequestHandler, HTTPServer


from src.path import root_join

host_name = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс, отвечающий за обработку входящих запросов от клиентов"""
    def do_get(self):
        """ Method for handling incoming GET requests """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(root_join('html_pages', 'contacts.html'), encoding='utf-8') as f:
            content = f.read()
        self.wfile.write(bytes(content, 'utf-8'))

    def do_post(self):
        """Способ обработки POST-запросов"""
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()


if __name__ == '__main__':
    web_server = HTTPServer((host_name, server_port),MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print('Server stopped')
