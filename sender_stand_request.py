import requests
import configuration
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)



def post_new_client_kit(kit_body,auth_token):
    headers_with_auth = data.headers.copy()
    headers_with_auth["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_with_auth)
