from dependencies import *

price_list = []
location_list = []
amenities_list = []
url_list = []

def extract_data_from_page(url:str):
    WINDOW_SIZE = "200,400"
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=driver_options)
    driver.get(url=url)

    price_tags = driver.find_elements(By.CLASS_NAME,"price-container")
    page_price_list = [tag.text for tag in price_tags]

    location_tags = driver.find_elements(By.CLASS_NAME,"property-name")
    page_location_list = [tag.text for tag in location_tags]

    detail_tags = driver.find_elements(By.CLASS_NAME,"detailed-info-container")

    for ul in detail_tags:
        li_tags = ul.find_elements(By.TAG_NAME,"li")
        amenities_list.append([tag.text for tag in li_tags])
    
    for i in range(len(page_price_list)):
        price_list.append(page_price_list[i])
        location_list.append(page_location_list[i])
        url_list.append(url)



def get_list_sub_pages(driver:webdriver)->list:
    # div id contaning links is : links-container-dt
    href_list = driver.find_element(By.ID,"links-container-dt")
    anchor_tags = href_list.find_elements(By.TAG_NAME,'a')
    page_urls = [tag.get_attribute("href") for tag in anchor_tags]
    return page_urls



if __name__ == "__main__":
    WINDOW_SIZE = "400,500"
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver_options.add_argument('--incognito')

    driver = webdriver.Chrome(options=driver_options)

    url = 'https://www.homes.com/'
    driver.get(url=url)

    data_list = []

    for page_number,page_url in enumerate(get_list_sub_pages(driver)):
        extracted_values = extract_data_from_page(page_url)
        if page_number == 10:
            break

    dataframe = {'url':url_list,'price':price_list,'location':location_list,'amenities':amenities_list}

    df = pd.DataFrame(dataframe)

    df.to_csv('homes.csv')

    config_url = open('mongo.conf','r').read()
    conn = pymongo.MongoClient(config_url)
    db = conn['SCRAP_DB']
    collection = db['homes_collection']

    for i in range(len(price_list)):
        collection.insert_one({
            "url":url_list,
            "price":price_list[i],
            "location":location_list[i],
            "amenities":amenities_list[i]
            })

    driver.close()






# print(anchor_tags)

# driver.close()

# price_list = driver.find_elements(By.CLASS_NAME,'property-price')
# # address
# address_list = driver.find_elements(By.CLASS_NAME,'property-address')
# # state zipcode
# state_zip_list = driver.find_elements(By.CLASS_NAME,"property-city-state-zip")

# price_list = [price.get_attribute("innerHTML") for price in price_list]
# address_list = [element.get_attribute("innerHTML") for element in address_list]
# state_zip_list = [element.get_attribute("innerHTML") for element in state_zip_list]

# location_list = address_list

# for index,value in enumerate(state_zip_list):
#     location_list[index] = location_list[index] + value




