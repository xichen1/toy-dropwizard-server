import requests

def test_system():
    r = requests.get('http://localhost:8085')
    json_request = r.json()
    assert(json_request['code'] == 404)

def test_message():
    r = requests.get('http://localhost:8085')
    json_request = r.json()
    assert(json_request['message'] == 'HTTP 404 Not Found')