from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

temp_list = []

def scrape():    
    page = requests.get(START_URL)
    soup = BeautifulSoup(page.text,"html.parser")
    table = soup.find_all("table", {"class":"wikitable sortable"})
    tr_tags = table[2].find_all('tr')
    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all('td')
        td_tag_text = [i.text.rstrip() for i in td_tags]
        temp_list.append(td_tag_text)

names = []
distance = []
mass =  []
radius = []
scraped_data = []

scrape()

for i in range(1,len(temp_list)):
    
    names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

    f = [names,distance,mass,radius]
    scraped_data.append(f)

headers = ['Star_Name','Distance','Mass','Radius']  

planet_df_1 = pd.DataFrame(list(zip(names,distance,mass,radius,)),columns=headers)

planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
