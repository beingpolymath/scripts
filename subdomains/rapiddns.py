import requests
import sys
from bs4 import BeautifulSoup

# Get the domain name from the command-line arguments
try:
    domain = sys.argv[1]
except IndexError:
    print("Please provide a domain name.")
    exit()

# Set the URL for fetching the subdomains
subdomain_url = f"https://rapiddns.io/subdomain/{domain}?full=1"

# Use requests to get the data from the URL
response = requests.get(subdomain_url)

# parse the HTML document using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# open the subdomain_name in write mode and write the data to it
subdomain_name=f"rapiddns-{domain}.txt"
with open(subdomain_name, 'w') as out:
    # find the <td> elements in the document
    td_elements = soup.find_all("td")


# print the contents of the <td> elements that contain a domain name
    for td in td_elements:
        if td.string and "." in td.string:
            print(td.string, file=out)

