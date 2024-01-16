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

    price_ = driver.find_elements(By.CLASS_NAME,"price-wrapper")




def get_list_sub_pages(driver:webdriver)->list:
    sub_urls = []
    div_container = driver.find_element(By.ID,"collapsed-772816318")
    anchor_tags = div_container.find_elements(By.TAG_NAME,"a")
    for tag in anchor_tags:
        sub_urls.append(tag.get_attribute("href"))
    return sub_urls



if __name__ == "__main__":
    WINDOW_SIZE = "400,500"
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver_options.add_argument('--incognito')

    driver = webdriver.Chrome(options=driver_options)

    url = "https://www.realtor.com/realestateforsale"
    driver.get(url=url)

    data_list = []

    for page_number,page_url in enumerate(get_list_sub_pages(driver)):
        extract_data_from_page(page_url)
        break
    

    driver.close()
    
    # dataframe = {'url':url_list,'price':price_list,'location':location_list,'amenities':amenities_list}

    # df = pd.DataFrame(dataframe)

    # df.to_csv('redfin.csv')

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
