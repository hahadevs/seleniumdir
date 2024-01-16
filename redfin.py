from dependencies import *

price_list = []
location_list = []
amenities_list = []
url_list = []

def extract_data_from_page(url:str):
    print("Extracting Data From : ",url)
    WINDOW_SIZE = "200,400"
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=driver_options)
    driver.get(url=url)
    # homecardV2Price
    price_spans = driver.find_elements(By.CLASS_NAME,"homecardV2Price")
    page_price_list = [tag.text for tag in price_spans]
    price_list.extend(page_price_list)
    
    address_spans = driver.find_elements(By.CLASS_NAME,"collapsedAddress")
    address_list = [tag.text for tag in address_spans]
    location_list.extend(address_list)

    feature_divs = driver.find_elements(By.CLASS_NAME,"HomeStatsV2")
    for div in feature_divs:
        div_tags = div.find_elements(By.CLASS_NAME,"stats")
        amenities_list.append([
            div_tags[0].text, # for beds
            div_tags[1].text, # for baths
            div_tags[2].text # for squarefoot
            ])
        url_list.append(url)
    driver.close()


def get_list_sub_pages(driver:webdriver)->list:
    sub_urls = []
    div_containers = driver.find_elements(By.CLASS_NAME,"EigenRegions")
    for index,div in enumerate(div_containers):
        if index == 2:break
        anchor_tags = div.find_elements(By.TAG_NAME,'a')
        page_urls = [tag.get_attribute("href") for tag in anchor_tags]
        sub_urls.extend(page_urls)
    return sub_urls



if __name__ == "__main__":
    WINDOW_SIZE = "400,500"
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver_options.add_argument('--incognito')

    driver = webdriver.Chrome(options=driver_options)

    url = 'https://www.redfin.com/'
    driver.get(url=url)

    data_list = []

    for page_number,page_url in enumerate(get_list_sub_pages(driver)):
        extract_data_from_page(page_url)
    
    driver.close()
    
    dataframe = {'url':url_list,'price':price_list,'location':location_list,'amenities':amenities_list}

    df = pd.DataFrame(dataframe)

    df.to_csv('redfin.csv')

    # config_url = open('mongo.conf','r').read()
    # conn = pymongo.MongoClient(config_url)
    # db = conn['SCRAP_DB']
    # collection = db['homes_collection']

    # for i in range(len(price_list)):
    #     collection.insert_one({
    #         "url":url_list,
    #         "price":price_list[i],
    #         "location":location_list[i],
    #         "amenities":amenities_list[i]
    #         })

    # driver.close()
