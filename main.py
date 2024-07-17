from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
# There are 9 products to be purchased.
is_auto = True
# COOKIE_URL = "https://orteil.dashnet.org/cookieclicker/"
COOKIE_URL = "https://orteil.dashnet.org/experiments/cookie/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(COOKIE_URL)

numof_cookies = driver.find_element(By.ID, "money")
# print(numof_cookies.text)

product_id_list = ["#buyCursor", "#buyGrandma", "#buyFactory", "#buyMine", "#buyShipment", "#buyAlchemy\\ lab", "#buyPortal", "#buyTime\\ machine"]
cursor = driver.find_element(By.CSS_SELECTOR, f"{product_id_list[0]} b")
cursor_cost = int(cursor.text.split(" ")[2])
grandma = driver.find_element(By.CSS_SELECTOR, f"{product_id_list[1]} b")
grandma_cost = int(grandma.text.split(" ")[2])
factory = driver.find_element(By.CSS_SELECTOR, f"{product_id_list[2]} b")
factory_cost = int(factory.text.split(" ")[2])
mine = driver.find_element(By.CSS_SELECTOR, f"{product_id_list[3]} b")
mine_cost = int(mine.text.split(" ")[2].replace(",", ""))
shipment = driver.find_element(By.CSS_SELECTOR, f"{product_id_list[4]} b")
shipment_cost = int(shipment.text.split(" ")[2].replace(",", ""))
alchemy = driver.find_element(By.CSS_SELECTOR, f"{product_id_list[5]} b")
alchemy_cost = int(alchemy.text.split(" ")[3].replace(",", ""))
portal = driver.find_element(By.CSS_SELECTOR, f"{product_id_list[6]} b")
portal_cost = int(portal.text.split(" ")[2].replace(",", ""))
timemachine = driver.find_element(By.CSS_SELECTOR, f"{product_id_list[7]} b")
timemachine_cost = int(timemachine.text.split(" ")[3].replace(",", ""))

product_list = [cursor, grandma, factory, mine, shipment, alchemy, portal, timemachine]
product_cost_list = [cursor_cost, grandma_cost, factory_cost, mine_cost, shipment_cost, alchemy_cost, portal_cost, timemachine_cost]
most_expensive_cost = max(product_cost_list)


def click_cookie():
    while is_auto:
        cookie_button = WebDriverWait(driver, 1000).until(
            EC.element_to_be_clickable((By.ID, "cookie"))
        )
        cookie_button.click()

def get_product_cost():
    while is_auto:

        time.sleep(10)
        for cost in product_cost_list:
            pass
            # print(f"This cost: {cost} and type of: {type(cost)}")

def purchase_product():
    mine_css = driver.find_element(By.CSS_SELECTOR, f"{product_id_list[3]} b")
    mine_xpath = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
    cursor_xpath = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')

    # Print the text content of both elements
    # print(f"CSS Selector (mine_css): {mine_css.text}")
    # print(f"XPath (mine_xpath): {mine_xpath.text}")

    # Compare their 'id' attributes if they exist
    css_id = mine_css.get_attribute('id')
    xpath_id = mine_xpath.get_attribute('id')
    mine_xpath.click()
    if css_id == xpath_id:
        print("Both selectors refer to the same element.")
    else:
        pass
        # print("The selectors refer to different elements.")
    # print(most_expensive_cost)
    while is_auto:
        time.sleep(1)
        # print(driver.find_element(By.XPATH, '//*[@id="buyMine"]').get_attribute('class'))
        # print(f'cursor attr: {cursor.get_attribute("class")}')
        # print(f'shipment attr:{shipment.get_attribute("class")}')
        # mine_xpath.click()
        cursor_xpath_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="buyCursor"]'))
        )
        cursor_xpath_button.click()

        # for product in product_list:
        #     pass
        #     if "grayed" in product.get_attribute("class"):
        #         print(f"{product} is not allowed")
        #     else:
        #         print(f"{product} is allowed")
        #         print(product.get_attribute("class").split())
                # print(product.get_attribute("class"))

# print(f"Most expensive: {most_expensive_cost}")

# print(numof_cookies.text)
# product_price_list = check_price()
# purchase_product(product_price_list)

click_thread = threading.Thread(target=click_cookie)
click_thread.start()

check_price_thread = threading.Thread(target=get_product_cost)
check_price_thread.start()

purchase_product_thread = threading.Thread(target=purchase_product)
purchase_product_thread.start()

