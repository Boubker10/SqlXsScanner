# main.py
from sql_injection_scanner import test_sql_injection, load_sql_payloads
from xss_scanner import test_xss_injection, load_xss_payloads
from utils import extract_forms
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)
def main():
    ascii_banner = pyfiglet.figlet_format("SQLXSSCANNER", font="slant")
    ascii_banner2 = pyfiglet.figlet_format("BY BOUBKER", font="slant")
    print(Fore.RED + ascii_banner)
    print(Fore.BLUE + ascii_banner2)
    url = input("Enter the URL to test for SQL Injection and XSS: ")
    sql_payloads = load_sql_payloads("payloads/sql_injection.txt")
    xss_payloads = load_xss_payloads("payloads/xss.txt")
    forms = extract_forms(url)
    print(f"Found {len(forms)} forms on {url}")
    for form in forms:
        print(f"Testing form at {form['action']}")
        params = {input['name']: "" for input in form['inputs']}
        sql_injection_vulnerable = test_sql_injection(url, params, sql_payloads)
        if sql_injection_vulnerable:
            print("Form is vulnerable to SQL Injection!")
        else:
            print("Form is not vulnerable to SQL Injection.")
        xss_vulnerable = test_xss_injection(url, params, xss_payloads)
        if xss_vulnerable:
            print("Form is vulnerable to XSS!")
        else:
            print("Form is not vulnerable to XSS.")
    
if __name__ == "__main__":
    main()
