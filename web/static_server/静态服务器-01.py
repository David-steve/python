import socket


# 静态服务器之返回固定页面
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
        print(recv_data)

        # 打开html文件
        with open("F:\\Share\\web\\01\\hello world.html", "r", encoding='UTF-8') as file:
            file_data = file.read()

        # 封装数据为http协议格式
        response_line = "HTTP/1.1 200 OK\r\n"
        response_head = 'Server: BWS/1.1\r\n'
        response_data = response_line + response_head + '\r\n' + file_data

        new_socket.send(response_data.encode('utf-8'))
        new_socket.close()
