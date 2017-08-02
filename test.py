# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random
import string
import HomePage
import unittest
import unicodedata

##### TO REMOVE

class SingInTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver')
		self.driver.get("https://www.goduo.com/")

	def test_create_new_user(self):
		home_page = HomePage.HomePageObject(self.driver)
		
		home_page.add_interests()
		home_page.add_birth_date()
		home_page.add_region()
		home_page.add_email("test@papapa.com")
		#self.driver.find_element_by_name(home_page.email).send_keys("roc.itxart@redbooth.com")
		home_page.add_username()
		home_page.add_password()
		home_page.click_register()

	def test_empty_data(self):
		home_page = HomePage.HomePageObject(self.driver)
		home_page.click_register()
		emptyDateText = self.driver.find_element_by_css_selector('div.tooltipOwn.birthDateDay').text
		assert emptyDateText == 'La fecha introducida es incorrecta'

		#Region already is set the first time you open the website, i.e. Valencia, seems a bug, forcing to be empty
		region = Select(self.driver.find_element_by_id(home_page.region))
		region.select_by_value(str(0))

		emptyRegionText = self.driver.find_element_by_css_selector('div.tooltipOwn.province').text
		assert emptyRegionText == u'No puede estar vacío'
		emptyEmailText = self.driver.find_element_by_css_selector('div.tooltipOwn.email').text
		assert emptyEmailText == u'El email no puede estar vacío'
		emptyUserNameText = self.driver.find_element_by_css_selector('div.tooltipOwn.userLogin').text
		assert emptyUserNameText == u'El usuario no puede estar vacío'
		emptyPasswordText = self.driver.find_element_by_css_selector('div.tooltipOwn.password').text
		assert emptyPasswordText == u'La contraseña no puede estar vacía'

	def test_show_repeated_email(self):
		home_page = HomePage.HomePageObject(self.driver)

		#Using an email already registered, to make the failure message appears, 
		home_page.add_email("test@papapa.com")
		home_page.click_register()
		alreadyUsedUserNameText = self.driver.find_element_by_css_selector('div.tooltipOwn.email').text
		assert alreadyUsedUserNameText == u'El email introducido ya está en uso'

	def tearDown(self):
		self.driver.quit()

if __name__=="__main__":
    unittest.main()