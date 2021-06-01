import socket


# 静态服务器之返回指定页面
if __name__ == '__main__':
    # 创建socket：IPV4，TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口号：8000
    server_socket.bind(("", 8000))
    server_socket.listen(128)

    while True:
        # 接收连接请求
        new_socket, ip_port = server_socket.accept()
        # 接收数据
        recv_data = new_socket.recv(4096)
        recv_content = recv_data.decode('utf-8')
        print(recv_content)

        if len(recv_content) == 0:
            new_socket.close()
            continue

        # 对数据进行分割，分割两次

        request_list = recv_content.split(' ', maxsplit=2)
        print(request_list[1])
        request_path = request_list[1]

        if request_path == '/':
            request_path = 'hello world.html'

        # 打开html文件
        # with open("F:\\Share\\web\\01\\hello world.html", "rb") as file:
        #     file_data = file.read()

        try:
            file = open(f'F:\\Share\\web\\01\\{request_path}', "rb")
        except IOError:
            response_line = "HTTP/1.1 404 NOT Found\r\n"
            file = open(f'F:\\Share\\web\\01\\erro.html', "rb")
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
        finally:
            file_data = file.read()
            file.close()

        # 封装数据为http协议格式
        response_head = 'Server: BWS/1.1\r\n'
        response_data = (response_line + response_head + '\r\n').encode('utf-8') + file_data

        new_socket.send(response_data)
        new_socket.close()
