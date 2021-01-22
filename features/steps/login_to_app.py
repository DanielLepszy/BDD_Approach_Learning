from behave import given, when, then

from BDD_Approach_Learning.core_implementation.page_models.page_models_factory.pages.login_page.login_page import LoginPageModel


@given('user open https://www.saucedemo.com/')
def test_given_impl(context):
    context.driver.get('https://www.saucedemo.com/')
    # home = HomeModel(context)


@when('set username: "{user_name}" and password: "{user_pass}" to inputs and click LOGIN button')
def test_given_impl(context, user_name, user_pass):
    LoginPageModel(context.driver).set_credentials_to_inputs(user_name, user_pass)


@then('system redirect page on https://www.saucedemo.com/inventory.html')
def test_step_impsl(context):
    assert context.driver.current_url == 'https://www.saucedemo.com/inventory.html'
