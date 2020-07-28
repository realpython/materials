import requests

# Replace the CLIENT_ID and CLIENT_SECRET below with your own.
client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"
redirect_uri = "https://httpbin.org/anything"
oauth_base_url = "https://github.com/login/oauth"
api_base_url = "https://api.github.com"


def get_code():
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "user",
        "response_type": "code",
    }

    endpoint = oauth_base_url + "/authorize"
    url = requests.get(endpoint, params=params).url
    print("Go to this URL and follow the OAuth flow there: %s" % url)
    code = input("code: ")
    return code


def get_token(code=None):
    endpoint = oauth_base_url + "/access_token"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "code": code,
    }
    headers = {"Accept": "application/json"}
    response = requests.post(endpoint, data=params, headers=headers).json()
    return response["access_token"]


def get_user(token=None):
    headers = {"Authorization": "token %s" % token}

    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers).json()
    return response


custom_code = get_code()
access_token = get_token(code=custom_code)
user = get_user(token=access_token)

name = user["name"]
username = user["login"]
private_repos_count = user["total_private_repos"]
print("%s (%s) | private repos: %s" % (name, username, private_repos_count))
