from selenium.webdriver.firefox.webdriver import WebDriver
from test.features.steps.browser_factory.browsers import Browsers


def before_all(context):
    print('ALLLL')
    context.driver = Browsers.get_driver()


# def after_all(context):  # cleanup after tests run
#     context.behave_driver.quit()
#

