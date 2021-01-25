import sys

from BDD_Approach_Learning.core_implementation.browser_factory.browsers import Browsers
from BDD_Approach_Learning.core_implementation.page_models.page_models_factory.page_models_factory import PageModelsFactory
from allure_behave.hooks import allure_report


def before_all(context):
    # print(sys.path)
    allure_report("BDD_Approach_Learning/features/report")
    context.driver = Browsers.get_driver()
    context.page_factory = PageModelsFactory(context.driver)


def after_feature(context, feature):
    '''Logout from app'''
    if feature.name != 'Log in to app with unpermitted user':
        context.page_factory.get_inventory_page().get_header_section().logout_from_app()
    # if feature.status.failure:
