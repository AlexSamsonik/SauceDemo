def test_open_login_page(inventory_page):
    assert inventory_page.url == inventory_page.inventory_page_url


def test_inventory_item_by_name(inventory_page):
    assert inventory_page.get_inventory_item_by_name("Sauce Labs Bolt T-Shirt")


def test_inventory_item_price(inventory_page):
    assert inventory_page.get_inventory_item_by_name("Sauce Labs Bolt T-Shirt").price == '$15.99'
