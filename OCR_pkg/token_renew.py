import requests

def get_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = ''
    response = requests.get(host)
    if response:
        res = response.json().get("refresh_token")
        return res
    return None

print(get_token())
