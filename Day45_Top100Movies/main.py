from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, "html.parser")

head_tag = soup.find_all(name="h3", class_="title")
top_movies = []

for name in head_tag:
    top_movies.append(name.getText())

top_movies.reverse()

with open("output.txt", "w", encoding="utf-8") as file:
    for movie in top_movies:
        file.write(str(movie)+"\n")