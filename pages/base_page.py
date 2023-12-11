from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def title(self) -> str:
        return self.driver.title

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def find_web_elements(self, *args) -> list[WebElement]:
        return self.driver.find_elements(*args)
