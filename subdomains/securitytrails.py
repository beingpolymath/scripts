import requests
import json
import argparse

def parse_args():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Fetch subdomains from SecurityTrails API')
    parser.add_argument('-d', '--domain', type=str, help='Target domain name', required=True)
    parser.add_argument('-t', '--api_key', type=str, help='API key for SecurityTrails API', required=True)
    parser.add_argument('-o', '--output', type=str, help='Output file for subdomains', default='subdomains.txt')
    args = parser.parse_args()

    domain = args.domain
    api_key = args.api_key
    output_file = args.output

    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    params = {"apikey": api_key}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        subdomains = response.json().get("subdomains", [])
        with open(output_file, "w") as f:
            for subdomain in subdomains:
                subdomain_text = f"{subdomain}.{domain}\n"
                f.write(subdomain_text)

        print(f"{len(subdomains)} subdomains written to {output_file}")

    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == '__main__':
    parse_args()
