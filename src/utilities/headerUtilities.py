

"""
This is API authorization header
We can use this incase the API headers change its easy to change it
"""


def url_header(token):
    header = {
        "Content-Type": "applycation/json",
        "login_user": token
    }
    return header