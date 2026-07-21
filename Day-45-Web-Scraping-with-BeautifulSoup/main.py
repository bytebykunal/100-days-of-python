import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies][::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    file.writelines('\n'.join(movie_titles))