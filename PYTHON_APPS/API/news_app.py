import requests
import news_mailer


topic = "tesla"
API_KEY ="ce6440d41d8046738ad04117bdc3c5af"
url = f'https://newsapi.org/v2/everything?' \
      f'q={topic}&' \
      f'from=2024-07-16&' \
      f'sortBy=publishedAt&' \
      f'apiKey={API_KEY}&' \
      f'language=en'
    

request = requests.get(url)
content = request.json()

body = 'Subject : Today"s News '
for article in content['articles'][:5]:
    length =  '='*(len(article['title']))    

    if article['title'] is not None:
        body = body + "\n" +article["title"] + "\n" + length + "\n" +str(article["description"]) + "\n" + article['url'] + 2*"\n"
        
body = body.encode("utf-8")

news_mailer.send_email(message=body)
     
        