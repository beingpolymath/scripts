import requests
import json
import sys

api_key = "test"

# Get the domain name from the command-line arguments
try:
    domain = sys.argv[1]
except IndexError:
    print("Please provide a domain name.")
    exit()


url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
params = {"apikey": api_key}

response = requests.get(url, params=params)

if response.status_code == 200:
    subdomains = response.json().get("subdomains", [])

    subdomain_name=f"securitytrails-{domain}.txt"
    with open(subdomain_name, "w") as f:
        for subdomain in subdomains:
            f.write(f"{subdomain}.{domain}\n")
            print(f"{subdomain}.{domain}")

else:
    print(f"Error {response.status_code}: {response.text}")


