import requests

if __name__ == "__main__":

    uri = "http://test.com/api"


    # Get Request Template
    response = request.get(
        uri,
        data={},
        headers={}
    )
    
    status_code = response.status_code
    body = response.json()

    print(status_code)
    print(body)
    