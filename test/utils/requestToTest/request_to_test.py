import requests

def request_to_test(verb, url, request_body='empty', key='empty', cookie='empty'):
    response = requests.request(
        verb,
        url=url,
        verify=False,
        headers={"Content-Type": "application/json", "x-api-key": f"{key}", "cookie": f"{cookie}"},
        timeout=15,
        json=request_body
    )
    return response