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

    driver.close()


def get_list_sub_pages(driver:webdriver)->list:
    sub_urls = []
    div = driver.find_elements(By.CLASS_NAME,"Text__TextContainerBase-sc-53dad1a1-1")
    print(len(div))
    # for anchor_tag in div.find_all(By.TAG_NAME,"a"):
    #     sub_urls.append(anchor_tag.get_attribute("href"))
    # print(sub_urls[1:])
    # return sub_urls[1:]

    return []



if __name__ == "__main__":
    WINDOW_SIZE = "400,500"
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    # driver_options.add_argument('--incognito')

    driver = webdriver.Chrome(options=driver_options)

    url = 'https://www.trulia.com/'
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
