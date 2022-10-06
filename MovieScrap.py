import requests 
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get(
    "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
)
soup = BeautifulSoup(page.content,'html.parser')
print(soup)
container = soup.find('tbody',class_="lister-list")

title = [name.find('a').get_text() for name in container.find_all(class_="titleColumn")]
release_year = [name.find('span').get_text() for name in container.find_all(class_="titleColumn")]
rating = [name.find('strong').get_text() for name in container.find_all(class_="ratingColumn imdbRating")]

top_rated_movies = pd.DataFrame({
        "title" : title,
        "Release Year" : release_year,
        "rating" : rating,
    })
    
print(top_rated_movies)
top_rated_movies.to_csv("top_rated_movies.csv")
