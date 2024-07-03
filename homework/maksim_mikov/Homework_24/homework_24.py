from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from time import sleep


@pytest.fixture()
def driver():
    firefox_options = Options()
    service = Service(GeckoDriverManager().install())
    firefox_options.set_capability("pageLoadStrategy", "none")  # "eager"
    firefox_driver = webdriver.Firefox(service=service, options=firefox_options)
    firefox_driver.maximize_window()
    yield firefox_driver
    sleep(3)


@pytest.fixture()
def driver2():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    sleep(3)


def test_add_product_to_cart(driver):
    product_name = 'Samsung galaxy s6'
    driver.get('https://www.demoblaze.com/index.html')

    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='prod.html?idp_=1']"))
    )
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='name']"))
    )
    assert result.text == product_name

    driver.find_element(By.XPATH, "//a[@onclick='addToCart(1)']").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])

    driver.find_element(By.ID, 'cartur').click()
    find_product = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'Samsung galaxy s6')]"))
    )
    assert find_product.text == product_name
    driver.close()


def test_add_product_to_cart_2(driver2):
    driver2.get('https://magento.softwaretestingboard.com/gear/bags.html')
    cards_of_products = WebDriverWait(driver2, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//li[@class='item product product-item']"))
    )
    compare_btn = cards_of_products[0].find_element(By.XPATH, "//a[@class='action tocompare']")
    name_product = cards_of_products[0].find_element(By.XPATH, "//a[contains(text(),'Push It Messenger Bag')]")
    driver2.execute_script("arguments[0].scrollIntoView(true);", name_product)

    actions = ActionChains(driver2)
    actions.move_to_element(cards_of_products[0])
    actions.move_to_element(compare_btn)
    actions.click()
    actions.perform()

    compare_block = driver2.find_element(By.XPATH, "//div[@class='block block-compare']")
    added_product = WebDriverWait(compare_block, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Push It Messenger Bag')]"))
    )
    assert name_product.text == added_product.text
