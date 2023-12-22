import requests
from bs4 import BeautifulSoup

def scrape_indian_express_urls():
    url = "https://indianexpress.com/"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor (a) tags on the page
        anchor_tags = soup.find_all('a')

        # Extract and store the URLs from the anchor tags
        urls = [a['href'] for a in anchor_tags if 'href' in a.attrs]

        return urls
    else:
        print("Failed to fetch the webpage.")
        return []

if __name__ == "__main__":
    extracted_urls = scrape_indian_express_urls()

    for url in extracted_urls:
        print(url)
import requests
from bs4 import BeautifulSoup

def scrape_indian_express_urls():
    url = "https://indianexpress.com/"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor (a) tags on the page
        anchor_tags = soup.find_all('a')

        # Extract and store the URLs from the anchor tags
        urls = [a['href'] for a in anchor_tags if 'href' in a.attrs]

        return urls
    else:
        print("Failed to fetch the webpage.")
        return []

if __name__ == "__main__":
    extracted_urls = scrape_indian_express_urls()

    for url in extracted_urls:
        print(url)
