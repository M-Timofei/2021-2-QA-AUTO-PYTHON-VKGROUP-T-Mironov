import settings
import socket

class SocketClient:

    def __init__(self):

        self.target_host = settings.MOCK_HOST
        self.target_port = int(settings.MOCK_PORT)

    def create_client(self, request):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        client.connect((self.target_host, self.target_port))
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

    def post_request(self, name):

        length = str(len(('{"name": "name_data"}'.replace('name_data', name))))
        request = f'POST /add_user HTTP/1.1\r\n' \
                  f'host: { self.target_host}\r\n' \
                  f'Content-Length: {length}\r\n'\
                  f'content-type: application/json\r\n'\
                  f'\r\n'\
                  '{"name": "data_name"}'.replace('data_name', name)

        return self.create_client(request)


    def get_request(self, name):

        request = f'GET /get_user/{name} HTTP/1.1\r\n' \
                  f'Host: { self.target_host}\r\n\r\n'

        return self.create_client(request)

    def put_request(self, name, new_job):

        length = str(len(
            ('{"new_job": :"data_new_job}'.replace('data_new_job', new_job))
             .encode()))
        request = f'PUT /change_user_by_name/{name} HTTP/1.1\r\n' \
                  f'host: { self.target_host}\r\n' \
                  f'Content-Length: {length}\r\n'\
                  f'content-type: application/json\r\n'\
                  f'\r\n'\
                  '{"new_job": "data_new_job"}'\
                  .replace('data_new_job', new_job)

        return self.create_client(request)

    def delete_request(self, name):

        request = f'DELETE /delete_user_by_name/{name} HTTP/1.1\r\n' \
                  f'Host: {self.target_host}\r\n\r\n'

        return self.create_client(request)