from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd

price_list = []
location_list = []
amenities_list = []
url_list = []

url = "https://www.makaan.com/"

def extract_data_from_page(url:str)->None:
    soup = BeautifulSoup(requests.get(url=url).text,'html.parser')

    divs = soup.find_all("div",{"data-type":"price-link"})
    for div in divs:
        price_span = div.find("span",{"class":"val"})
        price = "Rs." + price_span.find("meta",{"itemprop":"price"})['content']
        price_list.append(price)
    
    divs = soup.find_all("div",{"class":["title-line","mar-right"]})
    for div in divs:
        location = ""
        anchor_list = div.find_all("a",{"data-type":"projName","class":"projName"})
        for anchor_tag in anchor_list:
            for span in anchor_tag.find("span"):
                location += span.get_text()
        location_list.append(location)
            
    
    divs = soup.find_all("div",{"class":"infoWrap"})
    for div in divs:
        amenities = []
        li_list = div.find_all("li",{"class":"keypoint"})
        for li in li_list:
            span = li.find("span")
            if span is not None:
                amenities.append(span.get_text())
        amenities_list.append(amenities)
        url_list.append(url)
    

def get_url_list(soup:BeautifulSoup)->list:
    url_list = []
    footer = soup.find("footer")
    ul = footer.find("ul",{"class":"level1"})
    li_list = ul.find_all("li",{"data-type":"list-element"})
    li_list.pop(0)
    for li in li_list:
        anchor_list = li.find_all("a",href=True)
        for tag in anchor_list:
            url_list.append(tag['href'])
    return url_list

if __name__ == "__main__":

    response = requests.get(url=url)

    soup = BeautifulSoup(response.text,'html.parser')

    for index,page in enumerate(get_url_list(soup=soup)):
        if len(price_list) > 500:
            break
        print("Extracting Page : ",page)
        extract_data_from_page(page)
    

    dataframe = {'url':url_list,'price':price_list,'location':location_list,'amenities':amenities_list}

    df = pd.DataFrame(dataframe)

    df.to_csv('indus.csv')