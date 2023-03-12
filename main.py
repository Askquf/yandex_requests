import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Authorization': self.token}

    def upload(self, file_path: str):
        upload_place = requests.get(url='https://cloud-api.yandex.net/v1/disk/resources/upload', params={'path': file_path, 'overwrite': 'true'}, headers=self.get_headers()).json()['href']
        upload_res = requests.put(url=upload_place, data=open(file_path), headers=self.get_headers())
        upload_res.raise_for_status()
        if upload_res.status_code == 201:
            print('Succes!')


if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)