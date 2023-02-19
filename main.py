import requests

api_key='0bd9cab9007641548618130eeba010a7'
url='https://newsapi.org/v2/everything?q=tesla&from=2023-01-19&sortBy=publishedAt&apiKey=0bd9cab9007641548618130eeba010a7'

request=requests.get(url)
content=request.json()
for article in content["articles"]:
    print(article['title'])
    print(article['description'])

