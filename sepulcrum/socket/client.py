import socket
import ssl

from ..log import get_logger


class Client(object):
    def __init__(self, host, port, tls=True, encoding="UTF-8"):
        self.logger = get_logger(self.__class__.__name__)
        self.logger.debug("Creating socket to {}:{}".format(host, port))
        if tls:
            self.sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLS)
            self.sslcontext.verify_mode = ssl.CERT_NONE
            self.sslcontext.check_hostname = False
            self.socket = self.sslcontext.wrap_socket(
                socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            )
        else:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def send(self, text):
        self.logger.debug("Sending message: '{}'".format(text))
        self.socket.sendall("{}\n".format(text).encode(self.encoding))

    def recv(self, length=1024):
        self.logger.debug("Receiving message")
        self.response = self.socket.recv(length)
        self.logger.info(
            "Received: '{}'".format(self.response).encode(self.encoding)
        )  # noqa: E501

    def close(self):
        self.logger.debug("Closing socket.")
        self.socket.close()
