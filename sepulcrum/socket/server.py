import os

from ..log import get_logger

try:
    import SocketServer
except ImportError:
    # Python 3
    import socketserver as SocketServer


class BaseRequestHandler(SocketServer.BaseRequestHandler):
    def __init__(
        self, request, client_address, server, encoding="UTF-8", receive_size=1024
    ):
        super(BaseRequestHandler, self).__init__(request, client_address, server)
        self.logger = get_logger(self.__class__.__name__)
        self.encoding = encoding
        self.recv_size = receive_size

    def send_msg(self, msg):
        self.request.sendall(msg.encode(self.encoding))

    def recv_msg(self):
        return self.request.recv(self.recv_size).strip().decode(self.encoding)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


class ThreadedSSLTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def __init__(
        self,
        server_address,
        RequestHandlerClass,
        bind_and_activate=True,
        ssl_key_path=None,
        ssl_cert_path=None,
    ):
        """Constructor. May be extended, do not override."""
        SocketServer.TCPServer.__init__(
            self, server_address, RequestHandlerClass, False
        )

        dir = os.path.dirname(__file__)
        if ssl_key_path is None:
            key_file = os.path.join(dir, "server.key")
        elif not os.path.exists(ssl_key_path):
            raise ValueError("SSL key path {} does not exist.".format(ssl_key_path))
        else:
            key_file = ssl_key_path
        if ssl_cert_path is None:
            cert_file = os.path.join(dir, "server.crt")
        elif not os.path.exists(ssl_cert_path):
            raise ValueError("SSL cert path {} does not exist.".format(ssl_cert_path))
        else:
            cert_file = ssl_cert_path

        import ssl

        self.socket = ssl.wrap_socket(
            self.socket, keyfile=key_file, certfile=cert_file, cert_reqs=ssl.CERT_NONE
        )

        if bind_and_activate:
            self.server_bind()
            self.server_activate()
