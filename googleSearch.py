import requests
from bs4 import BeautifulSoup
import webbrowser

user_search = input("Search: ")
print("Googleing.........")

string = "https://www.google.com/search?q=" + user_search
user_agent = "Chrome/81.0.4044.129 Safari/537.36"

request_search_page = requests.get(string)

webbrowser.open(string)
