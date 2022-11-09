import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = s.getsockname()[0]
port = "5000"
bind = ":".join([ip,port])
reload = True
timeout = 300