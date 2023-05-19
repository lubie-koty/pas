import requests

http_response = requests.get('http://httpbin.org:80/image/png' )

if http_response.status_code == 200:
    with open('result.png', 'wb') as f:
        f.write(http_response.content)
    print('zapisano obraz')
else:
    print('blad przy polaczeniu ze strona')
