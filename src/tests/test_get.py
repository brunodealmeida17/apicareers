import requests


url_base_api = 'http://127.0.0.1:8000/careers/'
resultado = requests.get(url=url_base_api)


# Testing if the endpoint is correct.
assert resultado.status_code == 200

# Testing if the title of the first course is correct.
assert resultado.json()[0]['title'] == 'Software Engineer (Backend)'