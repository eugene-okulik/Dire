from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
# options.add_argument('start-maximized')
options.add_argument('--window-size=500,1080')
# чтобы браузер не закрывался сам
# options.add_experimental_option('detach', True)

# driver = webdriver.Firefox(options=options)
driver = webdriver.Chrome(options=options)
# sleep(3)
driver.get('https://www.google.kz/?hl=ru')
# driver.maximize_window()

# закрытие вкладки
# driver.close()
