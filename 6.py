import os
import requests

from datetime import datetime

url = '212.182.24.27:8080/image.jpg'

if os.path.exists('./image.jpg'):
    last_modified = datetime.fromtimestamp(os.path.getmtime('./image.jpg'))
else:
    last_modified = None
    
response = requests.head(url)
new_last_modified = response.headers.get('Last-Modified')

if last_modified is None or last_modified < datetime(new_last_modified):
    DATA_CHUNK = 1024 * 1024
    ranges = [
        (0, DATA_CHUNK - 1),
        (DATA_CHUNK, 2 * DATA_CHUNK - 1),
        (2 * DATA_CHUNK, None)
    ]

    with open('image.jpg', 'wb') as f:
        img = b''
        for start, end in ranges:
            headers = {'Range': f'bytes={start}-{end}' if end else f'bytes={start}-'}
            response = requests.get(url, headers=headers)
            img += response.content
        f.write(img)
