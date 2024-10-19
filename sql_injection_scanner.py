# sql_injection_scanner.py
import requests

def load_sql_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_sql_injection(url, params, sql_payloads):
    vulnerable = False
    for payload in sql_payloads:
        test_params = {key: payload for key in params.keys()}
        response = requests.get(url, params=test_params)
        
        if "syntax error" in response.text or "sql" in response.text.lower():
            print(f"Possible SQL Injection vulnerability found with payload: {payload}")
            vulnerable = True
    return vulnerable
