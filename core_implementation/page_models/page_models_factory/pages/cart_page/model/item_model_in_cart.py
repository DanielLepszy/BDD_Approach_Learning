from selenium.webdriver.remote.webelement import WebElement


class ItemModelInCart:

    def __init__(self, title, price, remove_btn, item_quantity) -> None:
        super().__init__()
        self.title: WebElement = title
        self.price: WebElement = price
        self.remove_btn: WebElement = remove_btn
        self.item_quantity: WebElement = item_quantity
