import requests


url_base_api = 'http://127.0.0.1:8000/careers/'



result = requests.delete(url=f'{url_base_api}5/')
assert result.status_code == 204

# Testing if the title of the first course is correct.
assert len(result.text) == 0