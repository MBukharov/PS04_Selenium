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
browser.find_element(By.ID,"searchButton").click()
while True:

    # search_line.send_keys(Keys.RETURN)
    selection = input("Выберите действие: \n1 - листать параграфы страницы\n2 - перейти на связанную страницу\nq - выйти\n")
    if selection == "1":
        paragraphs = browser.find_elements(By.TAG_NAME,"p")
        print("\nДля открытия следующего параграфа нажмите Enter. Для выхода введите q")
        for paragraph in paragraphs:
            print(paragraph.text)
            p = input()
            if p == 'q':
                break
    elif selection == "2":
        pass
    elif selection == "q":
        break

# time.sleep(5)