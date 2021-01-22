from core_implementation.browser_factory.browsers import Browsers
from core_implementation.page_models.page_models_factory.page_models_factory import PageModelsFactory


def before_all(context):
    context.driver = Browsers.get_driver()
    context.page_factory = PageModelsFactory(context.driver)


def after_feature(context, feature):
    '''Logout from app'''
    if feature.name != 'Log in to app with unpermitted user':
        context.page_factory.get_inventory_page().get_header_section().logout_from_app()
    if feature.status.failure:
        # TODO set allure report