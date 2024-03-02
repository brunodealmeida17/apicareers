import requests


url_base_api = 'http://127.0.0.1:8000/careers/'



result = requests.delete(url=f'{url_base_api}3/')
assert result.status_code == 204

# Testando se o título do primeiro curso está correto
assert len(result.text) == 0