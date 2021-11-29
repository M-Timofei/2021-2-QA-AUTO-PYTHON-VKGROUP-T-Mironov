import settings
import socket

class SocketClient:

    def post_request(self, name):

        target_host = settings.MOCK_HOST
        target_port = int(settings.MOCK_PORT)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        client.connect((target_host, target_port))
        length = str(len(('{"name": "name_data"}'.replace('name_data', name))))

        request = f'POST /add_user HTTP/1.1\r\n' \
                  f'host: {target_host}\r\n' \
                  f'Content-Length: {length}\r\n'\
                  f'content-type: application/json\r\n'\
                  f'\r\n'\
                  '{"name": "data_name"}'.replace('data_name', name)

        client.send(request.encode())

        total_data = []
        while True:
            data = client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        data = ''.join(total_data).splitlines()
        client.close()
        return data

    def get_request(self, name):

        target_host = settings.MOCK_HOST
        target_port = int(settings.MOCK_PORT)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.settimeout(0.1)

        client.connect((target_host, target_port))

        request = f'GET /get_user/{name} HTTP/1.1\r\n' \
                  f'Host: {target_host}\r\n\r\n'
        client.send(request.encode())

        total_data = []

        while True:
            data = client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()
        client.close()
        return data

    def put_request(self, name, new_job):

        target_host = settings.MOCK_HOST
        target_port = int(settings.MOCK_PORT)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        client.connect((target_host, target_port))
        length = str(len(
            ('{"new_job": :"data_new_job}'.replace('data_new_job', new_job))
             .encode()))

        request = f'PUT /change_user_by_name/{name} HTTP/1.1\r\n' \
                  f'host: {target_host}\r\n' \
                  f'Content-Length: {length}\r\n'\
                  f'content-type: application/json\r\n'\
                  f'\r\n'\
                  '{"new_job": "data_new_job"}'\
                  .replace('data_new_job', new_job)

        client.send(request.encode())

        total_data = []
        while True:
            data = client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        data = ''.join(total_data).splitlines()
        client.close()
        return data

    def delete_request(self, name):

        target_host = settings.MOCK_HOST
        target_port = int(settings.MOCK_PORT)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        client.connect((target_host, target_port))

        request = f'DELETE /delete_user_by_name/{name} HTTP/1.1\r\n' \
                  f'Host: {target_host}\r\n\r\n'
        client.send(request.encode())

        total_data = []

        while True:
            data = client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        client.close()
        data = ''.join(total_data).splitlines()
        return data