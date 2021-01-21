from behave import given, when, then

from test.features.steps.page_models.page_models_factory.page_models_factory import PageModelsFactory
from test.features.steps.page_models.page_models_factory.pages.login_page.login_page import LoginPageModel


@given('user log in to app using specified credentials: "{user_name}" and "{user_pass}"')
def test_given_impl(context, user_name, user_pass):
    context.driver.get('https://www.saucedemo.com/')
    context.login_page = context.page_factory.get_login_page()
    context.login_page.set_credentials_to_inputs(user_name, user_pass)

@when('user add two items to cart')
def test_when_impl(context):
    context.inventory_page = context.page_factory.get_inventory_page()
    context.inventory_section = context.inventory_page.get_inventory_section()
    context.inventory_section.add_to_cart_specified_items()
@when('click in shopping trolley icon to open cart')
def test_when_impl(context):
    print('s')

@then('user cart contain previous added items')
def test_step_impsl(context, error_message):
    print('s')
    # assert context.driver.current_url == 'https://www.saucedemo.com/'
