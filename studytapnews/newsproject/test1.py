# import requests
# from bs4 import BeautifulSoup

# # Define the URL of the Indian Express website
# indian_express_url = 'https://indianexpress.com/'

# # Send an HTTP GET request to the website
# response = requests.get(indian_express_url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content of the page using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find all anchor tags (links) in the HTML
#     anchor_tags = soup.find_all('a')

#     # Iterate through the anchor tags and extract the URLs
#     for tag in anchor_tags:
#         href = tag.get('href')

#         # Check if the URL is absolute (complete) or relative and make it absolute if necessary
#         if href and href.startswith('/'):
#             # Construct the absolute URL
#             full_url = indian_express_url + href
#         else:
#             full_url = href

#         # Print the URLs
#         print(full_url)
# else:
#     print("Failed to retrieve the web page. Status code:", response.status_code)
