from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/")
time.sleep(5)

