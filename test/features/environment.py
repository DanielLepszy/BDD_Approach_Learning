from behave import fixture

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


def before_all(context):
    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.message = 'message'

# def after_all(context):
#     context.browser.quit()


@fixture
def xx(context):
    return 22
