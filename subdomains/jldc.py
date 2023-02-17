import requests
import argparse
import json

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Fetch subdomains from jldc.me API')
parser.add_argument('-d', '--domain', type=str, help='Target domain name', required=True)
parser.add_argument('-o', '--output', type=str, help='Output file for subdomains', default='subdomains.txt')
args = parser.parse_args()

# Set the URL for fetching the subdomains
subdomain_url = f"https://jldc.me/anubis/subdomains/{args.domain}"

# Use requests to get the data from the URL
response = requests.get(subdomain_url)

# convert the JSON string back to a Python list
subdomains = json.loads(response.text)

# concatenate the subdomains into a single string,
# separated by newline characters
output = "\n".join(subdomains)

# Write the subdomains to the output file
with open(args.output, 'w') as f:
    f.write(output)

# Print the subdomains to the console
print(output)
