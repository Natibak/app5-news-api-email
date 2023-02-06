import requests

api_key = '4875704e4053411cbe67b0a8c6984f7a'
url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4875704e4053411cbe67b0a8c6984f7a'

# Make request
request = requests.get(url)

# Get a dictonary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

