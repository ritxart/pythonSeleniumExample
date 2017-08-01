from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver')
driver.get("https://www.goduo.com/")
driver.close()