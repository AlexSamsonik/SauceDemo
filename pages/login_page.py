from typing import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver, WebElement

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    # URL
    login_page_url = "https://www.saucedemo.com/"

    # Locators
    username_locator = (By.XPATH, "//*[@id='user-name']")
    password_locator = (By.XPATH, "//*[@id='password']")
    login_button_locator = (By.XPATH, "//*[@id='login-button']")
    error_message_locator = (By.XPATH, "//*[@class='error-message-container error']/h3")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def username_input(self) -> WebElement:
        return self.driver.find_element(*self.username_locator)

    @property
    def password_input(self) -> WebElement:
        return self.driver.find_element(*self.password_locator)

    @property
    def login_button(self) -> WebElement:
        return self.driver.find_element(*self.login_button_locator)

    @property
    def error_message(self) -> str:
        return self.driver.find_element(*self.error_message_locator).text

    def __login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    def open_login_page(self):
        self.driver.get(self.login_page_url)
        return self

    def success_login(self, username: str, password: str) -> InventoryPage:
        self.__login(username, password)
        return InventoryPage(self.driver)

    def unsuccess_login(self, username: str, password: str) -> Self:
        self.__login(username, password)
        return self
