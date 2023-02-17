import pytest

from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_base_link}/?promo=offer{no}" if no != 7
         else pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                           marks=pytest.mark.xfail)
         for no in range(10)]


@pytest.mark.parametrize('urls', links)
def test_guest_can_add_product_to_basket(browser, urls):
    link = urls
    page = ProductPage(browser, link)
    page.open()
    page.product_added()
