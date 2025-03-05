import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
Arquivo = "Arch.txt"
Hrefs = "Hrefs.txt"
extrasion_links = "Extracion.txt"

# 1° => define os argumentos dos Options
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument('--log-level=3')
# 2° => define o servico (Service)
service = Service('./chromedriver-win64/chromedriver-win64/chromedriver.exe')
# configura
driver = webdriver.Chrome(options=option,service=service)
# tente
try:
    driver.get('https://www.google.com/')
    driver.get('https://pt.wikipedia.org/wiki/Portal:Conte%C3%BAdo/Temas_gerais')
    while True:
        links = WebDriverWait(driver , 10).until(
            expected_conditions.presence_of_all_elements_located((By.TAG_NAME , "a"))
        )
        if len(links) > 0:
            with open(Arquivo , "w" , encoding="utf-8") as file:
                for num,i in enumerate(links):
                    file.write(f"[{num}] => '{i.get_attribute('href')}' \n")
            with open(Hrefs, "w" , encoding="utf-8") as file:
                for i in links:
                    file.write(f"{i.get_attribute('href')}\n")
        break
    driver.quit()
except ValueError:
    print(f"Error:{ValueError}")

driver = webdriver.Chrome(options=option,service=service)
driver.get('https://www.google.com/')
try:
    with open(Hrefs , "r") as file:
        urls = file.read().split()
        _FIRST,_LAST = [113,1391]
        while _FIRST < _LAST:
            driver.get(str(urls[_FIRST]))
            while True:
                body = WebDriverWait(driver , 1).until(
                    expected_conditions.presence_of_element_located((By.TAG_NAME, "body"))
                )
                if body:
                    url = driver.current_url
                    with open(extrasion_links , "a" , encoding="utf-8") as file:
                        file.write(f"{url} \n")
                    break
                break
            _FIRST = _FIRST + 1
except ValueError:
    print(ValueError)