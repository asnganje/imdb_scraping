from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option('detach', True)

url = ""
driver = webdriver.Chrome(options=options)
driver.get(url)