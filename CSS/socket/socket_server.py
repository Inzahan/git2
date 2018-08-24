import socket
import time


host = 'localhost'
port = 12345
buffer_size = 1024
addr = (host, port)


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    server_socket.listen(5)

    while True:
        print("Server is listening on {}:{}".format(host,port))
        client_socket, addr = server_socket.accept()
        print("Conneted: {}".format(addr))

        while True:
            data = client_socket.recv(buffer_size)
            if not data or data.decode('utf-8') == 'EXIT':
                break
            print("msg from client: {}".format(data.decode('utf-8')))
            to_send = time.ctime()
            print("sending client to: {}".format(to_send))

            try:
                client_socket.send(bytes(to_send, 'utf-8'))
            except:
                print("send failed")
        client_socket.close()
    server_socket.close()