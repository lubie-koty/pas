import requests

DATA_CHUNK = 1024 * 1024

url = '212.182.24.27:8080/image.jpg'
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
