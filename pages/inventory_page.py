import random
from typing import List, Union

from selenium.webdriver.common.by import By
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

    @property
    def price_only_number(self) -> str:
        return self.web_element.find_element(*self.price_locator).text.replace("$", "")


class InventoryPage(BasePage):
    # URL
    inventory_page_url = "https://www.saucedemo.com/inventory.html"

    # Locators
    inventory_items = (By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item']")

    def __collected_items(self) -> List[InventoryItem]:
        items: List[WebElement] = self.find_web_elements(*self.inventory_items)
        return [InventoryItem(item) for item in items]

    def get_inventory_item_by_name(self, name: str) -> Union[InventoryItem, None]:
        try:
            return [item for item in self.__collected_items() if item.name == name][0]
        except IndexError:
            print(f"WARNING: Item with name '{name}' not found in Inventory page.")
            return None

    def get_random_inventory_item(self) -> InventoryItem:
        return random.choice(self.__collected_items())
