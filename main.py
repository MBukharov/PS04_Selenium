from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/")
# time.sleep(5)

zapros = input("введите запрос: ")

search_line = browser.find_element(By.ID,"searchInput")
search_line.send_keys(zapros)
search_line.send_keys(Keys.RETURN)
time.sleep(5)