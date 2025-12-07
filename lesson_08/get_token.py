import requests

base_url = "https://ru.yougile.com"

def get_token(login, password):
    authentification = {
        'login': login,
        'password': password
    }
    company_list = requests.post(base_url+"/api-v2/auth/companies", json=authentification)
    authentification["companyId"] = company_list.json()["content"][0]["id"]
    token_response = requests.post(base_url+"/api-v2/auth/keys", json=authentification)
    return token_response.json()["key"]

login = ""
password = ""
print("Your token: ", get_token(login, password))
