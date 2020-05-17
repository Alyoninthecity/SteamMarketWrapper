from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
from json import JSONEncoder
import time
from array import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Item:
    def __init__(self, name, sell_price, N_sell, order_price, N_orders, URLImg, percGuad, guadagno):
        self.name = name  # nome
        self.order_price = order_price
        self.N_sell = N_sell
        self.N_orders = N_orders
        self.sell_price = sell_price  # prezzo piu` basso
        self.URLImg = URLImg  # URL immagine
        self.guadagno = guadagno
        self.percGuad = percGuad

    def __str__(self):
        return "nome: " + self.name + " N. pezzi in vendita: " + self.sell_listings + " Prezzo piu` basso:  " + + " URL immagine" + self.URLImg

    def dump(self):
        return {
            "Item": {
                'name': self.name, 'sell_price': self.sell_price, 'N_sell': self.N_sell, 'order_price': self.order_price, 'N_orders': self.N_orders, 'URLImg': self.URLImg, 'percGuad': self.percGuad, 'guadagno': self.guadagno
            }
        }


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://store.steampowered.com/login/?redir=%3Fl%3Ditalian&redir_ssl=1")

username = driver.find_element_by_id("input_username")
password = driver.find_element_by_id("input_password")

username.send_keys(input("Inserisci l'username di steam"))
password.send_keys(input("Inserisci la password di steam"))

driver.find_element(
    By.XPATH, '//*[@id="login_btn_signin"]/button/span').click()
codiceAuthI = input("Inserisci il codice dall'autenticatore")
auth = driver.find_element_by_id('twofactorcode_entry')
auth.send_keys(codiceAuthI)
driver.find_element(
    By.XPATH, '//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]/div[1]').click()

tableResult = []
time.sleep(1)
# print(//*[@id="searchResults_links"]/span[7])
for i in range(1, 4):
    print("primo")
    time.sleep(1)
    driver.get("https://steamcommunity.com/market/search?appid=252490" +
               "#p"+str(i)+"_popular_desc")
    delay = 3  # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, 'result_0_image')))
        linkP = driver.find_elements_by_class_name("market_listing_row_link")
        arraylink = [x.get_attribute("href") for x in linkP]
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    
    for link in arraylink:
        print("secondo")
        driver.get(link)
        try:
            myElem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mainContents"]/div[2]/div/div[1]/img')))
            print("Page is ready!")
            time.sleep(0.78)
            nome = (
                driver.find_element_by_id("largeiteminfo_item_name").text)
            img = (driver.find_element_by_xpath(
                '//*[@id="mainContents"]/div[2]/div/div[1]/img').get_attribute("src"))
            NVendita = (driver.find_element_by_xpath(
                '//*[@id="market_commodity_forsale"]/span[1]').text)
            prezzoVendita1 = (driver.find_element_by_xpath(
                '//*[@id="market_commodity_forsale"]/span[2]').text)

            NOrdine = (driver.find_element_by_xpath(
                '//*[@id="market_commodity_buyrequests"]/span[1]').text)
            prezzoOrdine1 = driver.find_element_by_xpath(
                '//*[@id="market_commodity_buyrequests"]/span[2]').text
            # ((3-(3*(13,03)/100))-5)/5
            prezzoVendita = float(
                prezzoVendita1[:-1].replace(",", ".").replace("-", "0"))
            prezzoOrdine = float(
                prezzoOrdine1[:-1].replace(",", ".").replace("-", "0"))
            percGuad = ((prezzoVendita-(prezzoVendita*13.03)/100) -
                        prezzoOrdine)/prezzoOrdine
            guadagno = (prezzoVendita-prezzoVendita*13.03/100) - prezzoOrdine
            tableResult.append(Item(nome, prezzoVendita1, NVendita,
                                    prezzoOrdine1, NOrdine, img, percGuad*100, guadagno))
        except TimeoutException:
            print("Loading took too much time!")
        except Exception:
            print("Errore")


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json.dumps([ob.dump() for ob in tableResult]),
              f, ensure_ascii=False, indent=4)
driver.close()
"""
ris = ""
l = ""


class Item:
    def __init__(self, name, sell_listings, sell_price, URLImg):
        self.name = name  # nome
        self.sell_listings = sell_listings  # numero pezzi in vendita
        self.sell_price = sell_price  # prezzo piu` basso
        self.URLImg = "https://steamcommunity-a.akamaihd.net/economy/image/" + \
            URLImg  # URL immagine

    def __str__(self):
        return "nome: " + self.name + " N. pezzi in vendita: " + self.sell_listings + " Prezzo piu` basso:  " + + " URL immagine" + self.URLImg


marketItems = []
time.sleep(3)
for i in range(0, 200, 100):
    driver.get(
        "https://steamcommunity.com/market/search/render/?appid=252490&norender=1&count=100&start="+str(i))
    ris = driver.find_element_by_tag_name("pre").text
    l = json.loads(ris)
    print(l["results"][0]["name"])
    for item in l["results"]:
        marketItems.append(Item(item.name, item.sell_listings,
                                item.sell_price, item.asset_description.icon_url_large))
"""
