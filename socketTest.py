import socket


def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)  # 设置超时时间
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0


host = 'localhost'  # 替换为你的Kafka服务器IP或域名
port = 9094
if check_port(host, port):
    print(f"Port {port} on {host} is open.")
else:
    print(f"Port {port} on {host} is closed or not reachable.")
