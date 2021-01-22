from core_implementation.browser_factory.browsers import Browsers
from core_implementation.page_models.page_models_factory.page_models_factory import PageModelsFactory


def before_all(context):
    context.driver = Browsers.get_driver()
    context.page_factory = PageModelsFactory(context.driver)

# def after_all(context):  # cleanup after tests run
#     context.behave_driver.quit()
#

