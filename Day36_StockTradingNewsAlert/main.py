import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "Alpha Vintage API"
NEWS_API_KEY = "NEWS API Key"
TWILIO_SID = 'twilio SID'
TWILIO_AUTH_TOKEN = 'Twilio Auth Key'

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percentage = round((difference / float(yesterday_closing_price)) * 100)



if abs(diff_percentage) > 5:
    
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title"
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]


    three_article = articles[:3]
  

    formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_article]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_='+16203123740',
            to='+917277682083'
        )
