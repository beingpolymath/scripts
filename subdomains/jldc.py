import requests
import re
import sys
import json

# Get the domain name from the command-line arguments
try:
    domain = sys.argv[1]
except IndexError:
    print("Please provide a domain name.")
    exit()

# Set the URL for fetching the subdomains
subdomain_url = f"https://jldc.me/anubis/subdomains/{domain}"

# Use requests to get the data from the URL
response = requests.get(subdomain_url)

# convert the JSON string back to a Python dictionary
y = json.loads(response.text)

# concatenate the elements of the list into a single string,
# separated by newline characters
output = "\n".join(y)

# print the resulting string
print(output)

# open the subdomain_name in write mode and write the data to it
subdomain_name=f"subdomain-{domain}.txt"

with open(subdomain_name, "w") as f:
    f.write(output)
