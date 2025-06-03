import time
from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get(url="https://cookieclicker.eu/experiments/cookie/")

the_time = 0

while True:
    time.sleep(5)
    the_time += 5
    if the_time % 300 == 0:
        print(driver.find_element(By.ID, "cps").text)

    cookie = driver.find_element(By.ID, "cookie")
    my_money = int(driver.find_element(By.ID, "money").text)

    cursor_button = driver.find_element(By.ID, "buyCursor")
    value_of_cursor = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split("-")[1].strip().replace(",", ""))

    grandma_button = driver.find_element(By.ID, "buyGrandma")
    value_of_grandma = int(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text.split("-")[1].strip().replace(",", ""))

    factory_button = driver.find_element(By.ID, "buyFactory")
    value_of_factory = int(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text.split("-")[1].strip().replace(",", ""))

    mine_button = driver.find_element(By.ID, "buyMine")
    value_of_mine = int(driver.find_element(By.CSS_SELECTOR, "#buyMine b").text.split("-")[1].strip().replace(",", ""))

    shipment_button = driver.find_element(By.ID, "buyShipment")
    value_of_shipment = int(driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text.split("-")[1].strip().replace(",", ""))

    alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
    value_of_alchemy_lab = int(driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[6]/b").text.split("-")[1].strip().replace(",", ""))

    portal_button = driver.find_element(By.ID, "buyPortal")
    value_of_portal = int(driver.find_element(By.CSS_SELECTOR, "#buyPortal b").text.split("-")[1].strip().replace(",", ""))

    time_machine_button = driver.find_element(By.ID, "buyTime machine")
    value_of_time_machine = int(driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[8]/b").text.split("-")[1].strip().replace(",",""))

    if my_money >= value_of_time_machine:
        time_machine_button.click()
    if my_money >= value_of_portal:
        portal_button.click()
    if my_money >= value_of_alchemy_lab:
        alchemy_lab.click()
    if my_money >= value_of_shipment:
        shipment_button.click()
    if my_money >= value_of_mine:
        mine_button.click()
    if my_money >= value_of_factory:
        factory_button.click()
    if my_money >= value_of_grandma:
        grandma_button.click()
    if my_money >= value_of_cursor:
        cursor_button.click()

