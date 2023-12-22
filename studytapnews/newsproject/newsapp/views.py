from django.shortcuts import render
import requests
from django.http import JsonResponse
from bs4 import BeautifulSoup
import html2text
import re

# Create your views here.

def combined_news (request):
    try:
        # Make an HTTP GET request to the Times of India for educational news.
        times_of_india_url = "https://timesofindia.indiatimes.com/rssfeeds/913168846.cms"
        response = requests.get(times_of_india_url)

        if response.status_code == 200:
            data = response.text
            # Parse the XML data (RSS feed) using BeautifulSoup to extract the news content.
            soup = BeautifulSoup(data, 'html.parser')
            items = soup.find_all('item')

            # Extract and process the text and image content of each news item.
            news_data = []
            for item in items:
                title = item.find('title').get_text()

                # Use html2text to convert HTML description to plain text
                description_html = item.find('description').get_text()
                h = html2text.HTML2Text()
                h.ignore_images = True
                description_text = h.handle(description_html)

                # Remove URLs from description_text
                description_text = re.sub(r'http\S+', '', description_text)

                # Use regular expressions to extract text without HTML tags
                description_text = re.sub(r'<[^>]*>', '', description_text)

                # Use regular expressions to extract image URLs
                image_urls = re.findall(r'src="([^"]+)"', description_html)

                link = item.find('link').get_text()

                news_data.append({
                    'title': title,
                    'description': description_text.strip(),  # Strip any leading/trailing spaces
                    'image_urls': image_urls,
                    'link': link,
                })

            return render(request, "newsapp/combined_news.html", {'news_data': news_data})
        else:
            return JsonResponse({'error': 'Failed to fetch data'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
