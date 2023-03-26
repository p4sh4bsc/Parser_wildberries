import requests
from bs4 import BeautifulSoup
import cloudscraper
import os
import time
from art import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import csv
from selenium.webdriver.common.keys import Keys 



options = webdriver.ChromeOptions()
options.headless=True
#options.add_argument("--no-sandbox")

id_of_cards = []
name_of_cards = []
price_of_cards = []
count_of_stars = []
delivery_dates = []

def get_website(item, page):
    
    url = 'https://www.wildberries.ru/catalog/0/search.aspx?page='+page+'&sort=popular&search='+item
    print(url)
    
    
    
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get(url)
        time.sleep(1)
        for i in range(100):
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(3)
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
            
    except Exception as ex:
        print(ex)
        
    finally:
        driver.close()
        driver.quit()
        
def get_cards():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    with open("index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    all_cards = soup.find("div", class_ = "product-card-list")
    cards = all_cards.find_all("div", class_ = "product-card j-card-item")
    
    for item in cards:
        
        ############# GET ID OF CARD #############
        id_of_card = item.get("data-nm-id")
        id_of_cards.append(id_of_card)
        ##########################################
        
        
        ############# GET NAME OF CARD #############
        name_of_card = item.find("span", class_="goods-name")
        name = (str(name_of_card.text)).replace("/","").strip()
        name_of_cards.append(name)
        ##########################################
        
        
        ############# GET PRICE OF CARD #############
        class_of_price = item.find("span", class_ = "price__lower-price")
        if class_of_price == None:
            class_of_price = item.find("ins", class_ = "price__lower-price")
        price = str(class_of_price.text)
        price = ''.join(price.split())
        price = price[0:-1]+"руб."
        price_of_cards.append(price)
        ##########################################
        
        
        ############# GET STARS OF CARD #############
        class_of_stars = item.find("span", class_ = "product-card__count")
        stars = str(class_of_stars.text)
        stars = ''.join(stars.split())
        count_of_stars.append(stars)
        ##########################################
        
        ############# GET DELIVERY-DATE OF CARD #############
        class_of_delivery_date = item.find("b", class_ = "product-card__delivery-date")
        delivery_date = (str(class_of_delivery_date.text)).strip()
        delivery_dates.append(delivery_date)

def create_csv():
    global date_for_excel
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_for_excel = date_now.replace(" ","_").replace(":", "-")
    with open(date_for_excel+".csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([" ID", "Название товара", "Цена товара", "Число отзывов", "Дата доставки"])
        
def load_data_to_csv():
    for i in range(len(id_of_cards)):
        list_of_data = []
        id = id_of_cards[i]
        name = name_of_cards[i]
        price = price_of_cards[i]
        stars = count_of_stars[i]
        date_d = delivery_dates[i]
        
        list_of_data.append(id)
        list_of_data.append(name)
        list_of_data.append(price)
        list_of_data.append(stars)
        list_of_data.append(date_d)
        with open(date_for_excel+".csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(list_of_data)

if __name__ == '__main__':
    tprint("Parser Wildberries")
    name_of_item = str(input("Введите название товара: "))
    #count_of_pages = str(input("Введите количество страниц для парсинга: "))
    get_website(name_of_item, "1")
    get_cards()
    create_csv()
    load_data_to_csv()
