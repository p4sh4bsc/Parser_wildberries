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
import argparse
import schedule

options = webdriver.ChromeOptions()
options.headless=True


arg = argparse.ArgumentParser(description='Сортировка по ценам и количеству звёзд')
arg.add_argument('-p', '--price', type=bool, const=True, default=False, nargs='?', help='Сортировка по убыванию цен')
arg.add_argument('-s', '--stars', type=bool, const=True, default=False, nargs='?', help='Сортировка по убыванию отзывов')
param = arg.parse_args()

def get_website(item, page):
    
    url = 'https://www.wildberries.ru/catalog/0/search.aspx?page='+str(page)+'&sort=popular&search='+item
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
    global id_of_cards
    global name_of_cards
    global price_of_cards
    global count_of_stars
    global delivery_dates
    global list_of_items
    
    id_of_cards = []
    name_of_cards = []
    price_of_cards = []
    count_of_stars = []
    delivery_dates = []
    
    list_of_items = []
    
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    with open("index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    all_cards = soup.find("div", class_ = "product-card-list")
    cards = all_cards.find_all("div", class_ = "product-card j-card-item")
    
    for item in cards:
        item_info = []
        ############# GET ID OF CARD #############
        try:
            id_of_card = item.get("data-nm-id")
        except:
            id_of_card = "Не указано"
        item_info.append(id_of_card)
        ##########################################
        
        
        ############# GET NAME OF CARD #############
        name_of_card = item.find("span", class_="goods-name")
        try:
            name = (str(name_of_card.text)).replace("/","").strip()
        except:
            name = "Не указано"
        item_info.append(name)
        ##########################################
        
        
        ############# GET PRICE OF CARD #############
        class_of_price = item.find("span", class_ = "price__lower-price")
        if class_of_price == None:
            class_of_price = item.find("ins", class_ = "price__lower-price")
        try:
            price = str(class_of_price.text)
            price = ''.join(price.split())
            price = price[0:-1]
            price = int(price)
        except:
            price = "Не указана"
        item_info.append(price)
        ##########################################
        
        
        ############# GET STARS OF CARD #############
        class_of_stars = item.find("span", class_ = "product-card__count")
        try:
            stars = str(class_of_stars.text)
            stars = ''.join(stars.split())
            stars = int(stars)
        except:
            stars = "Не указано"
        item_info.append(stars)   
        ##########################################
        
        ############# GET DELIVERY-DATE OF CARD #############
        class_of_delivery_date = item.find("b", class_ = "product-card__delivery-date")
        
        try:
            delivery_date = (str(class_of_delivery_date.text)).strip()
        except:
            delivery_date = "Не указана"
        item_info.append(delivery_date)
        list_of_items.append(item_info)

def create_csv():
    global date_for_excel
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_for_excel = date_now.replace(" ","_").replace(":", "-")
    with open("./for_csv/"+date_for_excel+".csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([" ID", "Название товара", "Цена товара", "Число отзывов", "Дата доставки"])
        
def load_data_to_csv():
    if param.price and param.stars:
        print("Укажите только один тип сортировки")
    elif param.price:
        list_of_items.sort(key=lambda x: x[2], reverse=True)
        print("sort by price")
    elif param.stars:
        list_of_items.sort(key=lambda x: x[3], reverse=True)
        print("sort by stars")
    
    for i in range(len(list_of_items)):
        
        with open("./for_csv/"+date_for_excel+".csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(list_of_items[i])

def get_and_save():
    create_csv()
    
        
    for i in range(count_of_pages):
        stats = os.stat("./for_csv/"+date_for_excel+".csv")
        if stats.st_size >= 10_536:
            print("creat new csv")
            create_csv()
        get_website(name_of_item, i)
        get_cards()
        load_data_to_csv()


if __name__ == '__main__':
    tprint("Parser Wildberries")
    name_of_item = str(input("Введите название товара: "))
    count_of_pages = int(input("Введите количество страниц для парсинга: "))
    time_to_launch = int(input("Через сколько часов запустить скрипт: "))
    
    schedule.every(time_to_launch).minutes.do(get_and_save)
    get_and_save()
    while True:
        schedule.run_pending()
