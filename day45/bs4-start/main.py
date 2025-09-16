from bs4 import BeautifulSoup
import lxml

import requests

response = requests.get("https://news.ycombinator.com/news")
wc_page = response.text
soup = BeautifulSoup(wc_page, "lxml")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.find('a')['href']
    article_links.append(article_link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_upvotes = article_upvotes.index(max(article_upvotes))
highest_upvotes_link = article_links[highest_upvotes]
highest_upvotes_text = article_texts[highest_upvotes]
print(highest_upvotes_text)
print(highest_upvotes_link)
