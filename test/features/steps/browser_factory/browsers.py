from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager


class Browsers:

    DRIVER: WebDriver = None

    # @classmethod
    # def get_driver(cls):
    #     return webdriver.Firefox(executable_path=GeckoDriverManager().install())

    @classmethod
    def get_driver(cls) -> WebDriver:
        browser_type = 'firefox'
        if browser_type == 'firefox':
            cls.DRIVER = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            return cls.DRIVER
        else:
            return cls.DRIVER
