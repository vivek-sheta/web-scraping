import requests
from bs4 import BeautifulSoup
import pandas as pd

title = []
year =  []
genre = []
ratting = []
size = 112

def get_data(obj):
    for name in obj:
        title.append(name.find('a').get_text().strip())     #title.append([ name.find('a').get_text().strip() for name in obj]) 
   
    for name in obj:
        year.append(name.find('span', class_='lister-item-year').get_text().strip())    #year.append([name.find('span', class_='lister-item-year').get_text().strip() for name in obj])
   
    for name in obj:
        genre.append(name.find('span', class_='genre').get_text().strip())        #genre.append([ name.find('span', class_='genre').get_text().strip() for name in obj])
    
    for name in obj:                #ratting.append([name.find('strong').get_text().strip() for name in obj if name.find('strong') != None])
        if name.find('strong') == None:  
            ratting.append(' ')
            continue
        ratting.append(name.find('strong').get_text().strip())
    
def change_page(): 
    first_page = requests.get("https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres=fantasy&explore=genres&ref_=adv_prv")
    soup = BeautifulSoup(first_page.content,'html.parser')
    content = soup.find_all(class_="lister-item-content")
    #while soup.find('div',class_='desc').find('a',class_='lister-page-next next-page')['href'] != None:
    for val in range(size): 
        get_data(content)
        request_page = requests.get("https://www.imdb.com/"+soup.find('div',class_='desc').find('a',class_='lister-page-next next-page')['href'])
        soup = BeautifulSoup(request_page.content,'html.parser')   
        content = soup.find_all(class_="lister-item-content")
        print(val)

def make_csv():
    data = pd.DataFrame({
            "title" : title,
            "year" : year,
            "genre" : genre,
            "ratting" : ratting,
        })
    print(data)
    data.to_csv("top_tv_shows.csv")
    
def main():
    change_page()
    make_csv()

if __name__ == "__main__":
    main()
