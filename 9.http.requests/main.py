import requests
from nice import nice_print as nprint

def test_request():
    url = "https://httpbin.org/get"
    response = requests.get(url)

    if response.status_code == 200:
        print("OK")
    nprint(response.content)

if __name__ == "__main__":
    test_request()
