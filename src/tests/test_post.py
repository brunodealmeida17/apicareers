import requests



url_base_api = 'http://127.0.0.1:8000/careers/'
resultado = requests.get(url=url_base_api)


new_careers = {
        "username": "brunodealmeida17",
        "title": "DevOps Engineer",
        "content": "We are seeking a DevOps Engineer to manage and automate our infrastructure. Responsibilities include deploying, automating, maintaining, and managing production systems on AWS or other cloud platforms."
    
    }

resultado = requests.post(url=url_base_api, data=new_careers)


# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['title'] == new_careers['title']