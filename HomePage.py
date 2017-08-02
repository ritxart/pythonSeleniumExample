import random
import string
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class HomePageObject(BasePage):
	#Form locators
	iam = ["femaleSoy", "maleSoy"]
	looking =  ["femaleBusco", "maleBusco"]
	birthdayDay = 'birthDateDay'
	birthdayMonth = 'birthDateMonth'
	birthdayYear = 'birthDateYear'
	region = 'provinceregion'
	email = 'email'
	user = 'userLogin'
	password = 'password'
	register = 'register'

	def add_interests(self):
		sex = [random.randint(0,1), random.randint(0,1)]
		iam = self.driver.find_element(By.XPATH, "//label[@for='" + self.iam[sex[0]] + "']").click()
		looking = self.driver.find_element(By.XPATH, "//label[@for='" + self.looking[sex[1]] + "']").click()

	def add_email(self, email):
		self.driver.find_element_by_name(self.email).send_keys(email)

	def add_birth_date(self):
		birth_date = [random.randint(1,31),random.randint(1,12),random.randint(1937,1999)]

		day = Select(self.driver.find_element_by_name(self.birthdayDay))
		day.select_by_value(str(birth_date[0]))
		
		month = Select(self.driver.find_element_by_name(self.birthdayMonth))
		month.select_by_value(str(birth_date[1]).zfill(2))
		
		year = Select(self.driver.find_element_by_name(self.birthdayYear))
		year.select_by_value(str(birth_date[2]))

	def add_region(self):
		region = Select(self.driver.find_element_by_id(self.region))
		region.select_by_value(str(random.randint(1,50)).zfill(2))

	def add_username(self):
		user = self.driver.find_element_by_name(self.user).send_keys(''.join(random.sample(string.ascii_lowercase, 10)))

	def add_password(self):
		password = self.driver.find_element_by_name(self.password).send_keys(''.join(random.sample(string.ascii_lowercase, 10)))
	
	def click_register(self):
		self.driver.find_element_by_name(self.register).click()	