from selenium.webdriver.remote.webelement import WebElement


class InventoryCardModel:

    def __init__(self, image_element, add_card_element, price_element, item_title) -> None:
        super().__init__()
        self.image: WebElement = image_element
        self.add_card_button: WebElement = add_card_element
        self.price: WebElement = price_element
        self.item_title: WebElement = item_title
