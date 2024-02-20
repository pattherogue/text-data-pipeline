import requests
import json

def fetch_news(api_key, sources, language='en', page_size=100):
    """
    Fetch news articles from the News API.

    Args:
        api_key (str): Your News API key.
        sources (list): List of news sources to retrieve articles from.
        language (str): Language code for articles (default is 'en' for English).
        page_size (int): Number of articles per page (default is 100).

    Returns:
        list: List of dictionaries representing news articles.
    """
    url = 'https://newsapi.org/v2/everything'
    articles = []

    for source in sources:
        params = {
            'apiKey': api_key,
            'sources': source,
            'language': language,
            'pageSize': page_size
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            articles.extend(data.get('articles', []))
        else:
            print(f"Failed to fetch articles from {source}. Status code: {response.status_code}")

    return articles

def save_articles_to_json(articles, filename):
    """
    Save articles to a JSON file.

    Args:
        articles (list): List of articles (dictionaries).
        filename (str): Name of the JSON file to save.
    """
    with open(filename, 'w') as f:
        json.dump(articles, f, indent=4)

if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'
    sources = ['bbc-news', 'cnn', 'the-new-york-times']
    articles = fetch_news(api_key, sources)
    print(f"Total articles retrieved: {len(articles)}")
    save_articles_to_json(articles, 'news_articles.json')
