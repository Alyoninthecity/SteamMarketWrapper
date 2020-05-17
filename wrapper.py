from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from array import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
# print(//*[@id="searchResults_links"]/span[7])
for i in range(1, 3):
    print("primo")
    time.sleep(1)
    driver.get("https://steamcommunity.com/market/search?appid=252490" +
               "#p"+str(i)+"_popular_desc")
    time.sleep(1)
    linkP = driver.find_elements_by_class_name("market_listing_row_link")
    arraylink = [x.get_attribute("href") for x in linkP]
    for link in arraylink:
        print("secondo")
        driver.get(link)
        tableResult.append([])
        tableResult[-1].append(driver.find_element_by_id("largeiteminfo_item_name").text)
        time.sleep(1)
        tableResult[-1].append(driver.find_element_by_xpath(
            '//*[@id="market_commodity_forsale"]/span[2]').text)
        tableResult[-1].append(driver.find_element_by_xpath(
            '//*[@id="market_commodity_buyrequests"]/span[2]').text)
print(tableResult)
