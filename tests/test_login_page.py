import pytest

from pages.inventory_page import InventoryPage


def test_open_login_page(login_page):
    actual_login_page_title = (login_page
                               .open_login_page()
                               .title)
    assert actual_login_page_title == "Swag Labs"


def test_login_with_valid_credentials(login_page):
    inventory_page: InventoryPage = (login_page
                                     .open_login_page()
                                     .success_login("standard_user", "secret_sauce"))
    assert inventory_page.current_url == inventory_page.inventory_page_url


@pytest.mark.parametrize('username, password, error_msg', [
    ("", "", "Epic sadface: Username is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("user@example.com", "invalid_pass", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "secret_sauceX", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_userX", "secret_sauce", "Epic sadface: Username and password do not match any user in this service")
]
                         )
def test_login_with_invalid_credentials(username, password, error_msg, login_page):
    actual_error_msg = (login_page
                        .open_login_page()
                        .unsuccess_login(username, password)
                        .error_message)
    assert actual_error_msg == error_msg
