# xss_scanner.py
import requests

def load_xss_payloads(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def test_xss_injection(url, params, xss_payloads):
    vulnerable = False
    for payload in xss_payloads:
        test_params = {key: payload for key in params.keys()}
        response = requests.get(url, params=test_params)
        if payload in response.text:
            print(f"Possible XSS vulnerability found with payload: {payload}")
            vulnerable = True
    return vulnerable
