import argparse
import requests
from bs4 import BeautifulSoup


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Fetch subdomains from RapidDNS API')
    parser.add_argument('-d', '--domain', type=str, help='Target domain name', required=True)
    parser.add_argument('-o', '--output', type=str, help='Output file for subdomains', default='subdomains.txt')
    args = parser.parse_args()

    domain = args.domain
    output_file = args.output

    # Set the URL for fetching the subdomains
    subdomain_url = f"https://rapiddns.io/subdomain/{domain}?full=1"

    # Use requests to get the data from the URL
    response = requests.get(subdomain_url)

    # parse the HTML document using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # open the subdomain_name in write mode and write the data to it
    subdomain_name = f"rapiddns-{domain}.txt"
    with open(output_file, 'w') as out:
        # find the <td> elements in the document
        td_elements = soup.find_all("td")

        # print the contents of the <td> elements that contain a domain name
        for td in td_elements:
            if td.string and "." in td.string:
                subdomain = td.string.strip()
                if subdomain:
                    subdomain_text = f"{subdomain}"
                    print(subdomain_text, file=out)


if __name__ == '__main__':
    main()
