import requests

http_response = requests.get(
    'http://httpbin.org:80/html',
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
)

if http_response.status_code == 200:
    with open('result.html', 'w') as f:
        f.write(http_response.text)
    print('zapisano strone')
else:
    print('blad przy polaczeniu ze strona')
