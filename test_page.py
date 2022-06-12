from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
from pages.locators import *

link = "https://www.yandex.ru"

def open_market():
    market = browser.find_element(*MainPageLocators.MARKET_ICON)
    market.click()

def open_electronics_page():
    electronics = browser.find_element(*MarketPageLocators.ELECTRONICS_LINK)
    electronics.click()
  
def open_phones_page():
    phones = browser.find_element(*ElectronicsPageLocators.PHONES_LINK)
    phones.click()
    
def open_filters():
    filters = browser.find_element(*PhonesPageLocators.ALL_FILTERS)
    filters.click()

def set_max_price():
    max_price = browser.find_element(*FiltersPageLocators.MAX_PRICE)
    max_price.send_keys('20000')
  
def set_screen_diagonal():
    diagonal_expand = browser.find_element(*FiltersPageLocators.DIAGONAL_EXPAND)
    browser.execute_script("arguments[0].scrollIntoView();", diagonal_expand)
    diagonal_expand.click()
    diagonal_input = browser.find_element(*FiltersPageLocators.DIAGONAL_INPUT)
    diagonal_input.send_keys('3')    
    
def select_popular_brands():
    brands = ['Apple', 'ASUS', 'Google', 'HONOR', 'HUAWEI', 'Nokia', 'Samsung', 'vivo', 'Xiaomi']
    expand_brands = browser.find_element(*FiltersPageLocators.MORE_BRANDS)
    expand_brands.click()
    available_brands = list(brands)
    #remove unavailable brands
    for i in brands:
        try:
            path1 = f"//label/input[@disabled][@value='{i}']"
            browser.implicitly_wait(3)
            browser.find_element_by_xpath(path1)
            available_brands.remove(f'{i}')
        except NoSuchElementException:
            pass

    #select 5 random brands
    random_brands = random.sample(available_brands, 5)
    print("Выбранные марки: ")
    print(random_brands)
    for i in random_brands:
        path2 = f"//label/input[@value='{i}']"
        brand = browser.find_element_by_xpath(path2)
        browser.execute_script("arguments[0].click();", brand)

def show_offers():
    show = browser.find_element(*FiltersPageLocators.SHOW_BUTTON)
    show.click()

def get_first_product_name():
    global phone_name 
    phone_name = browser.find_element(*PhonesPageLocators.FIRST_PRODUCT).text
    print("Выбранный смартфон: " + phone_name)

def change_sorting():
    sort_by_price = browser.find_element(*PhonesPageLocators.SORT_BY)
    sort_by_price.click()
    time.sleep(2)

'''def find_selected_product():
    phone_path = f"//span[contains(.,'{phone_name}')]"
    browser.implicitly_wait(3)
    selected_phone = browser.find_element_by_xpath(phone_path)
    selected_phone.click()'''


def find_phone():
    global phone_is_found
    phone_is_found = False
    while phone_is_found == False:
        try:
            browser.implicitly_wait(2)
            phone_path = f"//span[contains(.,'{phone_name}')]"
            phone = browser.find_element_by_xpath(phone_path)
            browser.execute_script("arguments[0].click();", phone)
            #phone.click()
            phone_is_found = True
        except NoSuchElementException:
            try:
                show_more = browser.find_element(*PhonesPageLocators.SHOW_MORE)
                show_more.click() 
            except NoSuchElementException:
                print(f"Ошибка: после изменения сортировки {phone_name} не найден")
                break

def get_rating():
    rating = browser.find_element(*PhonesPageLocators.RATING)
    rating_text = browser.execute_script('return arguments[0].textContent;', rating)
    print("Рейтинг смартфона: " + rating_text)  

browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.maximize_window() 
browser.get(link)
default_tab = browser.window_handles[0]
open_market()
market_tab = browser.window_handles[1]
browser.switch_to.window(market_tab)
open_electronics_page()
open_phones_page()
open_filters()
set_max_price()
set_screen_diagonal()
select_popular_brands()
show_offers()
get_first_product_name()
change_sorting()
find_phone()
if phone_is_found == True:
    product_tab = browser.window_handles[2]
    browser.switch_to.window(product_tab)
    get_rating()
time.sleep(2)
browser.quit()
