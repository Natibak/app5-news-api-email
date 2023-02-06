import requests
from send_email import send_email

api_key = '4875704e4053411cbe67b0a8c6984f7a'
url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4875704e4053411cbe67b0a8c6984f7a'

# Make request
request = requests.get(url)

# Get a dictonary with data
content = request.json()

# Access the article titles and description
body =''
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

