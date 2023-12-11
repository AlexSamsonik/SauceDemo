from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class InventoryItem:
    # Locators
    item_name_locator = (By.XPATH, ".//div[@class='inventory_item_name ']")
    price_locator = (By.XPATH, ".//div[@class='inventory_item_price']")
    button_add_to_cart_locator = (By.XPATH, ".//button[@class='btn btn_primary btn_small btn_inventory ']")

    def __init__(self, web_element: WebElement):
        self.web_element = web_element

    @property
    def name(self) -> str:
        return self.web_element.find_element(*self.item_name_locator).text

    @property
    def button_add_to_cart(self) -> WebElement:
        return self.web_element.find_element(*self.button_add_to_cart_locator)

    @property
    def price(self) -> str:
        return self.web_element.find_element(*self.price_locator).text


class InventoryPage(BasePage):
    # URL
    inventory_page_url = "https://www.saucedemo.com/inventory.html"

    # Locators
    inventory_items = (By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def url(self):
        return self.driver.current_url

    def __collected_items(self) -> List[InventoryItem]:
        items: List[WebElement] = self.driver.find_elements(*self.inventory_items)
        return [InventoryItem(item) for item in items]

    def get_inventory_item_by_name(self, name: str) -> Union[InventoryItem, None]:
        try:
            return [item for item in self.__collected_items() if item.name == name][0]
        except IndexError:
            print(f"WARNING: Item with name '{name}' not found in Inventory page.")
            return None
