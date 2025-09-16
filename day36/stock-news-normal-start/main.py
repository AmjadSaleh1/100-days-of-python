import os
import requests
from twilio.rest import Client
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("auth_token")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = os.getenv("API_KEY")
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in stock_data.items()]
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
Y_close = float(data_list[0]['4. close'])
day_before = float(data_list[1]['4. close'])
difference = abs(Y_close - day_before)
up_down = None
if difference > 0:
    up_down = "ג¬†ן¸"
elif difference < 0:
    up_down = "ג¬‡ן¸"
diff_percentage = round((difference / Y_close) * 100)

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


if abs(diff_percentage) > 1:
    News_Paramters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    New_response = requests.get(NEWS_ENDPOINT, params=News_Paramters)
    article = New_response.json()["articles"]
    three_articles = article[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
    formated_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percentage}%\nheadline: {article['title']}.\nBrief: {article['description']}" for
        article in
        three_articles]

    client = Client(account_sid, auth_token)
    for art in formated_articles:
        message = client.messages.create(
            body=art,
            from_="+14159388935",
            to="+18777804236",
        )
        print(message.status)

