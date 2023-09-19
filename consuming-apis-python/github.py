import requests

# First, make sure to follow the steps to create your own GitHub application:
# https://docs.github.com/en/free-pro-team@latest/developers/apps/creating-an-oauth-app


# REPLACE the following variables with your Client ID and Client Secret
CLIENT_ID = "<REPLACE_WITH_CLIENT_ID>"
CLIENT_SECRET = "<REPLACE_WITH_CLIENT_SECRET>"

# REPLACE the following variable with what you added in the
# "Authorization callback URL" field.
REDIRECT_URI = "<REPLACE_WITH_REDIRECT_URI>"


# In this method you'll ask the GitHub API for a URL to redirect the user
# for authentication.
def create_oauth_link():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user",
        "response_type": "code",
    }

    # This endpoint is defined in the GitHub documentation:
    # https://docs.github.com/en/free-pro-team@latest/developers/apps/authorizing-oauth-apps#1-request-a-users-github-identity
    endpoint = "https://github.com/login/oauth/authorize"

    response = requests.get(endpoint, params=params)

    # When you make the request above, GitHub will redirect you to their
    # website to input your credentials. Since you're doing this
    # programmatically, you need to get the `url` parameter and print it in
    # the console instead.
    return response.url


# In this method you'll exchange the code you got from the GitHub API with
# an access token.
def exchange_code_for_access_token(code=None):
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }

    # Here you define the content type you're expecting to get.
    # In this case – JSON.
    headers = {"Accept": "application/json"}

    # This endpoint is defined in the GitHub documentation:
    # https://docs.github.com/en/free-pro-team@latest/developers/apps/authorizing-oauth-apps#2-users-are-redirected-back-to-your-site-by-github
    endpoint = "https://github.com/login/oauth/access_token"

    response = requests.post(endpoint, params=params, headers=headers).json()
    return response["access_token"]


# Finally in this method you'll print the user information re. its name,
# username and number of private repositories.
def print_user_info(access_token=None):
    # Now you need to send the `access_token` in the headers
    # when calling the API.
    headers = {"Authorization": f"token {access_token}"}

    # This endpoint is defined in the GitHub documentation:
    # https://docs.github.com/en/free-pro-team@latest/rest/reference/users#get-the-authenticated-user
    endpoint = "https://api.github.com/user"

    response = requests.get(endpoint, headers=headers).json()

    # The response will be a dictionary with multiple user-related field.
    # You can try `print(response)` to see all of them.
    name = response["name"]
    username = response["login"]
    private_repos_count = response["total_private_repos"]
    print(
        f"{name} ({username}) | "
        f"number of private repositories: {private_repos_count}"
    )


# So, one last time, step by step:
# 1. Create a link to redirect the user to for authentication:
link = create_oauth_link()
print(f"Follow the link to start the authentication with GitHub: {link}")

# 2. Paste the code you got from GitHub after authenticating
code = input("GitHub code: ")

# 3. Exchange that code with an access token
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} with access token: {access_token}")

# 4. Fetch user information
print_user_info(access_token=access_token)
