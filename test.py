from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random
import string
import HomePage
import unittest

##### TO REMOVE

class SingInTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver')
		self.driver.get("https://www.goduo.com/")

	def test_create_new_user(self):
		home_page = HomePage.HomePageObject()
		birth_date = [random.randint(1,31),random.randint(1,12),random.randint(1937,1999)]
		
		sex = [random.randint(0,1), random.randint(0,1)]
		iam = self.driver.find_element(By.XPATH, "//label[@for='" + home_page.iam[sex[0]] + "']").click()
		looking = self.driver.find_element(By.XPATH, "//label[@for='" + home_page.looking[sex[1]] + "']").click()

		day = Select(self.driver.find_element_by_name(home_page.birthdayDay))
		day.select_by_value(str(birth_date[0]))
		
		month = Select(self.driver.find_element_by_name(home_page.birthdayMonth))
		month.select_by_value(str(birth_date[1]).zfill(2))
		
		year = Select(self.driver.find_element_by_name(home_page.birthdayYear))
		year.select_by_value(str(birth_date[2]))

		region = Select(self.driver.find_element_by_id(home_page.region))
		region.select_by_value(str(random.randint(1,50)).zfill(2))

		## MODIFYYYYY !!!!
		email = self.driver.find_element_by_name(home_page.email).send_keys("roc.itxart@redbooth.com")
		
		user = self.driver.find_element_by_name(home_page.user).send_keys(''.join(random.sample(string.ascii_lowercase, 10)))

		password = self.driver.find_element_by_name(home_page.password).send_keys(''.join(random.sample(string.ascii_lowercase, 10)))
		self.driver.find_element_by_name("register").click()
	def tearDown(self):
		self.driver.quit()

if __name__=="__main__":
    unittest.main()