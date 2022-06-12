from selenium.webdriver.common.by import By

class MainPageLocators():
    MARKET_ICON = (By.XPATH, "//a[@data-id='market']")

class MarketPageLocators():   
    ELECTRONICS_LINK = (By.XPATH, "//span[contains(.,'Электроника')]")
    
class ElectronicsPageLocators():
    PHONES_LINK = (By.XPATH, "//li/div/a[contains(.,'Смартфоны')]")
    
class PhonesPageLocators():
    ALL_FILTERS = (By.XPATH, "//span/span[contains(.,'Все фильтры')]")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div[data-index='1'] span[data-tid='2e5bde87']")
    SORT_BY = (By.CSS_SELECTOR, "[data-autotest-id='dprice']")
    SHOW_MORE = (By.XPATH, "//span[contains(.,'Показать ещё')]")
    RATING = (By.CSS_SELECTOR, "._11U2d span._2v4E8")
    
class FiltersPageLocators():
    MAX_PRICE = (By.XPATH, "//div[@data-filter-id='glprice']//div[2]/input")
    DIAGONAL_EXPAND = (By.XPATH, "//div[@data-filter-id='14805766']//h4")
    DIAGONAL_INPUT = (By.XPATH, "//div[@data-filter-id='14805766']//div[1]/input")
    MORE_BRANDS = (By.XPATH, "//button[@class='zsSJk dOdmr _1QJa9']")
    BRANDS_INPUT = (By.XPATH, "//div[@data-filter-id='7893318']//input[@class='_34OG2']")
    FIRST_ELEMENT = (By.XPATH, "//div[@data-tid='46a32646']")
    SHOW_BUTTON = (By.XPATH, "//a[contains(.,'Показать')]")

