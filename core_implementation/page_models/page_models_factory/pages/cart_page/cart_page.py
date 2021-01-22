from seleniumpagefactory import PageFactory
from selenium import webdriver

from core_implementation.page_models.page_models_factory.pages.cart_page.model.item_model_in_cart import ItemModelInCart


class UserCartPageModel(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        # self.highlight = True

    locators = {
        "cart_items": ('CSS', '.cart_item'),
        "continue_shopping_button": ('CSS', '.cart_footer a[href$="./inventory.html"]'),
        "checkout_button": ('CSS', '.cart_footer a[href$="./checkout-step-one.html"]'),
        "error_header": ('CSS', 'h3[data-test="error"]'),
    }

    def get_item_list_model_in_cart(self) -> list[ItemModelInCart]:
        item_list: list[ItemModelInCart] = []
        for cart_item in self.cart_items:
            # item_title = cart_item.find_element_by_xpath("/descendant::*[contains(@class,'inventory_item_name')]")
            # item_price = cart_item.find_element_by_xpath("/descendant::*[contains(@class,'inventory_item_price')]")

            item_title = cart_item.find_element_by_xpath('.inventory_item_name')
            item_price = cart_item.find_element_by_xpath('.inventory_item_price')
            item_remove_button = cart_item.find_element_by_xpath("/descendant::button[text()='remove']")
            item_quantity = cart_item.find_element_by_css(".cart_quantity")
            item_list.append(ItemModelInCart(item_title, item_price, item_remove_button, item_quantity))

        return item_list
