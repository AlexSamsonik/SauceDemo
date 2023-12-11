import pytest
from selenium import webdriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def driver():
    """
    Fixture for setting up and closing webdriver in session scope.

    Setting:
     - Set maximum size for window.
     - Set implicitly wait as 5 seconds.
    """

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver) -> LoginPage:
    return LoginPage(driver)


@pytest.fixture()
def inventory_page(login_page) -> InventoryPage:
    return (login_page
            .open_login_page()
            .success_login("standard_user", "secret_sauce"))
