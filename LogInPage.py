from HomePage import BasePage

class LogInPageObject(BasePage):
	#Form locators
	username = 'user'
	password = 'passwd'
	entrarButton = 'login'

	def add_username(self, usern):
		self.driver.find_element_by_name(self.username).send_keys(usern)

	def add_pwd(self, pwd):
		self.driver.find_element_by_name(self.password).send_keys(pwd)

	def click_login_button(self):
		self.driver.find_element_by_name(self.entrarButton).click()

	def do_login(self, usr, pwd):
		self.add_username(usr)
		self.add_pwd(pwd)
		self.click_login_button()