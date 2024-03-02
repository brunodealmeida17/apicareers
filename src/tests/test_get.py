import requests


url_base_cursos = 'http://127.0.0.1:8000/careers/'
resultado = requests.get(url=url_base_cursos)


# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando se o título do primeiro curso está correto
assert resultado.json()[0]['title'] == 'Python Jr/mid - backend'