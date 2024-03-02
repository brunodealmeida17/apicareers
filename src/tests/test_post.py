import requests



url_base_api = 'http://127.0.0.1:8000/careers/'
resultado = requests.get(url=url_base_api)


new_careers = {        
        "username": "brunodealmeida17",
        "title": "Blockchain Developer",
        "content": "We are seeking a Blockchain Developer to design, implement, and maintain blockchain-based applications. Experience with blockchain platforms like Ethereum, Hyperledger, or Corda is preferred."
    }
    

result = requests.post(url=url_base_api, data=new_careers)


# Testing the HTTP status code 201.
assert result.status_code == 201

# Testing if the returned course title matches the one provided.
assert result.json()['title'] == new_careers['title']