import socket

class Sterling:
    def __init__(self, host='localhost', port=9162, decode_responses=True):
        self.host = host
        self.port = port
        self.decode_responses = decode_responses
        self.socket = None
        self.connect()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def _send_command(self, command):
        self.socket.sendall((command + '\n').encode())
        response = self.socket.recv(4096).decode().strip()
        if self.decode_responses:
            return response
        return response.encode()

    def set(self, key, value):
        response = self._send_command(f"SET {key} {value}")
        return response == "OK"

    def get(self, key):
        response = self._send_command(f"GET {key}")
        return None if response == "(nil)" else response

    def delete(self, key):
        response = self._send_command(f"DEL {key}")
        return response == "OK"

    def exists(self, key):
        response = self._send_command(f"EXISTS {key}")
        return response == "1"

    def expire(self, key, seconds):
        response = self._send_command(f"EXPIRE {key} {seconds}")
        return response == "OK"

    def ttl(self, key):
        response = self._send_command(f"TTL {key}")
        return int(response)

    def keys(self):
        response = self._send_command("KEYS")
        return response.split() if response != "(empty)" else []

    def close(self):
        if self.socket:
            self.socket.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
