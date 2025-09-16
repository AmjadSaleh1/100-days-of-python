import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
best_m = response.text
soup = BeautifulSoup(best_m, "lxml")
m_headlines = soup.find_all(name="h3", class_="title")
# Write your code below this line 👇
m_headlines_text = [headline.getText() for headline in soup.find_all(name="h3", class_="title")]
#used pop to remove elements from the list because there is error in the typo from the website
m_headlines_text.pop(41)
m_headlines_text.pop(15)
m_headlines_text.reverse()

with open("movies.txt", "w") as file:
    for movie in m_headlines_text:
        file.write(f"{movie}\n")
