from seleniumpagefactory import PageFactory

from BDD_Approach_Learning.core_implementation.page_models.page_models_factory.pages.inventory_page.sections.model.card_model import InventoryCardModel


class InventorySection(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # locators = {
    #     "shopping_counter": ('CSS', '.fa-layers-counter shopping_cart_badge')
    # }

    def get_card_item_elements(self) -> list[InventoryCardModel]:
        items = self.driver.find_elements_by_css_selector('.inventory_item')
        all_elements = []

        for item in items:
            add_card_element = item.find_element_by_css_selector('.btn_inventory')
            image_element = item.find_element_by_css_selector('.inventory_item_img img')
            price_element = item.find_element_by_css_selector('.pricebar')
            item_title = item.find_element_by_css_selector('.inventory_item_name')
            item_model = InventoryCardModel(image_element, add_card_element, price_element, item_title)
            all_elements.append(item_model)

        return all_elements

    def add_to_cart_specified_items(self, items_name: list):
        available_items_on_page = self.get_card_item_elements()

        for cart_model in available_items_on_page:
            if cart_model.item_title.text in items_name:
                cart_model.add_card.click()
