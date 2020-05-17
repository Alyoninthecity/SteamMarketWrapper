from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://store.steampowered.com/login/?redir=%3Fl%3Ditalian&redir_ssl=1")

username = driver.find_element_by_id("input_username")
password = driver.find_element_by_id("input_password")

username.send_keys(input("Inserisci l'username di steam"))
password.send_keys("Inserisci la password di steam")

driver.find_element(
    By.XPATH, '//*[@id="login_btn_signin"]/button/span').click()
codiceAuthI = input("Inserisci il codice dall'autenticatore")
auth = driver.find_element_by_id('twofactorcode_entry')
auth.send_keys(codiceAuthI)
driver.find_element(
    By.XPATH, '//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]/div[1]').click()
time.sleep(3)
driver.get("https://steamcommunity.com/market/search?appid=252490")
 div#id="searchResultsRows"->foreach(a.class="market_listing_row_link"){href}
