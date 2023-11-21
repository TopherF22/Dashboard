from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    # Replace 'YOUR_API_KEY' with your actual API key
    newsapi = NewsApiClient(api_key='7d28cc5d8b874e1584c4ee8801ac738f')

    # Check if a search query is present in the request
    search_query = request.GET.get('q', '')

    if search_query:
        # If there is a search query, use /v2/everything endpoint
        search_results = newsapi.get_everything(q=search_query)
        articles = search_results['articles']
    else:
        # If no search query, fetch top headlines
        top_headlines = newsapi.get_top_headlines(sources='reuters')
        articles = top_headlines['articles']

    news_titles = []
    descriptions = []
    images = []
    publishedAt = []
    source = []
    url = []

    for article in articles:
        news_titles.append(article['title'])
        descriptions.append(article['description'])
        images.append(article['urlToImage'])
        publishedAt.append(article['publishedAt'])
        source.append(article['source']['name'])
        url.append(article['url'])


    news_list = zip(news_titles, descriptions, images, publishedAt, source, url)

    return render(request, 'news.html', context={"mylist": news_list, "search_query": search_query})
