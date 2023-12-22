from django.shortcuts import render
import requests
from django.http import JsonResponse
from bs4 import BeautifulSoup 
import html2text
import re 
# Create your views here.
def index_page(request):
    return render(request,"newsapp/index.html")
def fetch_10th_class_news(request):
    try:
        # List of RSS feed URLs for multiple news sources
        rss_feed_urls = [
            # "https://tv9telugu.com/feed",
            # "https://telugu.samayam.com/langapi/sitemap/gstandrssfeed/48238599.xml",
            # "https://www.andhrajyothy.com/rss/gn/education/feed.xml",
            # "https://hittvtelugu.com/feed",
            "https://telugu.news18.com/nodeapi/v1/tel/sitemap/today",
           
            # "https://tv9telugu.com/feed",
            # "https://www.teluguglobal.com/feed",
            # "https://www.thehindu.com/sci-tech/science/?service=rss",

            # "https://www.weareteachers.com/feed/",
            # "https://ntvtelugu.com/feed",
            # "https://ww2.kqed.org/mindshift/feed/",
            # "https://timesofindia.indiatimes.com/rssfeeds/4118235.cms",
            # "https://telugu.hindustantimes.com/rss/telangana",
            # "https://timesofindia.indiatimes.com/rssfeeds/-2128816011.cms",
            # # "https://indianexpress.com/feed",
            # "https://telugu.hindustantimes.com/rss/telangana.cms",
            # "https://www.amarujala.com/rss/maharashtra.xml",
            # "https://www.theweek.in/education/admissions.rss.html",
            # "https://www.theweek.in/education/exams.rss.html",
            # "https://timesofindia.indiatimes.com/rssfeeds/913168846.cms",
            # Add your RSS feed URLs here
        ]

        # Collect news data from all RSS feeds
        news_data = []
        for rss_feed_url in rss_feed_urls:
            response = requests.get(rss_feed_url)

            if response.status_code == 200:
                data = response.text
                # Parse the XML data (RSS feed) using BeautifulSoup to extract the news content.
                soup = BeautifulSoup(data, 'xml')  # Use 'xml' parser for RSS feeds
                items = soup.find_all('item')

                # Extract and process the text, video, and image content of each news item.
                for item in items:
                    title = item.find('title').get_text()
                    description_html = item.find('description').get_text()

                    # Extract image URLs from the description
                    description_soup = BeautifulSoup(description_html, 'html.parser')
                    image_urls = [img['src'] for img in description_soup.find_all('img')]

                    # Check if image URLs are available
                    media_url = image_urls[0] if image_urls else None

                    link = item.find('link').get_text()

                    # Append news item to the list
                    news_data.append({
                        'title': title,
                        'media_url': media_url,
                        'link': link,
                        'description': description_html
                    })

        # Render the news data in the template
        return render(request, "newsapp/school_news.html", {'news_data': news_data})

    except Exception as e:
        # Return an error response in case of an exception
        return JsonResponse({'error': str(e)}, status=500)


        
def IndiaExpress(request):
    try:
        # Make an HTTP GET request to The Indian Express for educational news.
        indian_express_url = "https://indianexpress.com/education/"
        response = requests.get(indian_express_url)

        if response.status_code == 200:
            data = response.text
            # Parse the HTML data to extract the news content.
            soup = BeautifulSoup(data, 'html.parser')
            articles = soup.find_all('article')

            # Extract and process the title, description, and image content of each news article.
            news_data = []
            for article in articles:
                title = article.find('h2').get_text()
                description = article.find('p').get_text()

                # Extract image URL from the article, if available.
                image = article.find('img')
                image_url = image['src'] if image else None

                link = article.find('a')['href']

                news_data.append({
                    'title': title,
                    'description': description,
                    'image_url': image_url,
                    'link': link,
                })

            return render(request, "newsapp/education_news.html", {'news_data': news_data})
        else:
            return JsonResponse({'error': 'Failed to fetch data'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

   

