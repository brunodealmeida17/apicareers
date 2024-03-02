import requests



url_base_api = 'http://127.0.0.1:8000/careers/'
result = requests.get(url=url_base_api)


update_careers = {
        "username": "brunodealmeida17",
        "title": "Software Engineer (Backend)",
        "content": "We are looking for a Software Engineer with a focus on backend development. Responsibilities include designing and implementing scalable software solutions using languages like Java, Python, or C++."
    }

result = requests.put(url=f'{url_base_api}2/', data=update_careers)


# Testing the HTTP status code.
assert result.status_code == 200

# Testing the title
assert result.json()['title'] == update_careers['title']