import requests

URL = 'http://httpbin.org/html'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
FILE_NAME = 'pliczek.html'


def download_html():
    try:
        response = requests.get(url=URL, headers={'User-Agent': USER_AGENT})
        response.raise_for_status()
        with open(FILE_NAME, 'w') as f:
            f.write(response.text)
    except requests.exceptions.RequestException as e:
        print(f'Error: {str(e)}')


if __name__ == '__main__':
    download_html()
