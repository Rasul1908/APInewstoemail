import requests
from emailsender import send_email
topic='chatgpt'
api_key='0bd9cab9007641548618130eeba010a7'
url='https://newsapi.org/v2/everything?' \
    f'q={topic}&from=2023-02-19&sortBy=publishedAt&' \
    'apiKey=0bd9cab9007641548618130eeba010a7&language=en'

request=requests.get(url)
content=request.json()
body =''
for article in content["articles"][:20]:
    if article['title'] is not None and article['description'] is not None :

        body="Subject: Today's news" \
             + "\n" + body+ article['title'] \
             + '\n' + article['description'] \
             + '\n'\
             + article['url'] +2* '\n'

body=body.encode('utf-8')

send_email(body)
print(body)



