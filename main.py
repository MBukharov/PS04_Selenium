from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Открытие начальной страницы Википедии
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/")

#Ввод первоначального запроса
zapros = input("введите запрос: ")
search_line = browser.find_element(By.ID,"searchInput")
search_line.send_keys(zapros)
browser.find_element(By.ID,"searchButton").click()
# search_line.send_keys(Keys.RETURN)

#Бесконечный цикл основной программы
while True:
    selection = input("Выберите действие: \n1 - листать параграфы страницы\n2 - перейти на связанную страницу\nq - выйти\n")
    if selection == "1":

        #Находим основные параграфы и выводим на экран
        paragraphs = browser.find_elements(By.TAG_NAME,"p")
        print("\nДля открытия следующего параграфа нажмите Enter. Для выхода введите q")
        for paragraph in paragraphs:
            print(paragraph.text)
            p = input()
            if p == 'q':
                break
    elif selection == "2":
        links = []
        links_name = []
        #Находим ссылки на связанные страницы
        for element in browser.find_elements(By.TAG_NAME,"div"):
            if element.get_attribute("class") == "hatnote navigation-not-searchable":
                link = element.find_element(By.TAG_NAME,"a").get_attribute("href")
                link_name = element.find_element(By.TAG_NAME,"a").text
                links.append(link)
                links_name.append(link_name)

        #Если ссылки нашлись, просим пользователя ввести номер необходимой ссылки
        if links_name:
            print("Выберите нужную страницу:")
            for i,l in enumerate(links_name):
                print(f"{i+1} - {l}")
            p = int(input("\n"))
            browser.get(links[p-1])

        #Если ссылок нет, просим ввести новый поисковый запрос или выйти
        else:
            print("Связанные страницы отсутствуют. Введите поисковый запрос или q для выхода: ")
            p = input()
            if p == "q":
                break
            else:
                search_line = browser.find_element(By.ID, "searchInput")
                search_line.send_keys(p)
                browser.find_element(By.ID, "searchButton").click()

    elif selection == "q":
        break
