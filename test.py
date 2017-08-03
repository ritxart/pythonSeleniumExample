# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
import string
import HomePage
import LogInPage
import unittest
import unicodedata

class SingInTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver')
		self.driver.get("https://www.goduo.com/")

	def test_create_new_user(self):
		home_page = HomePage.HomePageObject(self.driver)
		
		home_page.add_interests()
		home_page.add_birth_date()
		home_page.add_region()
		email = (''.join(random.sample(string.ascii_lowercase, 10))) + '@testing.com'
		home_page.add_email(email)
		username = home_page.add_username()
		home_page.add_password()
		home_page.click_register()
		activation_url = self.driver.current_url
		assert activation_url == 'https://www.goduo.com/activacion'
		activationPageText = self.driver.find_element_by_css_selector('h1.account__title.account__title--accent').text
		assert activationPageText == 'Ya casi has terminado ' + username

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

		#Using an email already registered, to make the failure message appears. 
		home_page.add_email("test@papapa.com")
		home_page.click_register()
		alreadyUsedUserNameText = self.driver.find_element_by_css_selector('div.tooltipOwn.email').text
		assert alreadyUsedUserNameText == u'El email introducido ya está en uso'

	def test_short_parameters(self):
		home_page = HomePage.HomePageObject(self.driver)
		home_page.add_username(3)
		home_page.add_password(3)
		home_page.click_register()
		shortUserNameText = self.driver.find_element_by_css_selector('div.tooltipOwn.userLogin').text
		assert shortUserNameText == u'El usuario introducido es demasiado corto'
		shortPasswordText = self.driver.find_element_by_css_selector('div.tooltipOwn.password').text
		assert shortPasswordText == u'La contraseña introducida es demasiado corta'

	def test_log_in(self):

		#Using and email registered to erify log in flow
		home_page = HomePage.HomePageObject(self.driver)
		login_page = LogInPage.LogInPageObject(self.driver)
		home_page.click_already_user()
		login_url = self.driver.current_url
		assert login_url == 'https://www.goduo.com/login'
		login_page.do_login('testinggoduo@gmail.com','papapa22')
		menuButton = self.driver.find_element_by_id('openMenuMobile')
		self.assertTrue(menuButton.is_displayed())

	def tearDown(self):
		self.driver.quit()

if __name__=="__main__":
    unittest.main()