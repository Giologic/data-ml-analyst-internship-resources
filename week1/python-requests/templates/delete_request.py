import requests

if __name__ == "__main__":

    uri = "http://test.com/api"


    # Delete Request Template
    response = requests.delete(
        uri,
        data={},
        headers={}
    )

    status_code = response.status_code
    body = response.json()

    print(status_code)
    print(body)
    