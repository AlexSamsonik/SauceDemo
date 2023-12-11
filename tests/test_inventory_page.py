import pytest

expected_inventory_item_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                                 "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]


def test_open_login_page(inventory_page):
    assert inventory_page.current_url == inventory_page.inventory_page_url


def test_inventory_item_by_name(inventory_page):
    assert inventory_page.get_inventory_item_by_name("Sauce Labs Bolt T-Shirt")


def test_inventory_item_price(inventory_page):
    assert inventory_page.get_inventory_item_by_name("Sauce Labs Bolt T-Shirt").price == "$15.99"


def test_inventory_item_price_only_number(inventory_page):
    assert inventory_page.get_inventory_item_by_name("Sauce Labs Bolt T-Shirt").price_only_number == "15.99"


def test_get_random_inventory_item(inventory_page):
    assert inventory_page.get_inventory_item_by_name("Sauce Labs Bolt T-Shirt").name in expected_inventory_item_names


@pytest.mark.parametrize('index, name', [(0, expected_inventory_item_names[0]),
                                         (1, expected_inventory_item_names[1]),
                                         (2, expected_inventory_item_names[2]),
                                         (3, expected_inventory_item_names[3]),
                                         (4, expected_inventory_item_names[4]),
                                         (5, expected_inventory_item_names[5])
                                         ]
                         )
def test_inventory_item_by_index(index, name, inventory_page):
    assert inventory_page.get_inventory_item_by_index(index).name == name
