from behave import given, when, then

from test.features.steps.page_models.page_models_factory.pages.login_page.login_page import LoginPageModel


@given('unpermitted user open https://www.saucedemo.com/')
def test_given_impl(context):
    context.driver.get('https://www.saucedemo.com/')


@when('set wrong username: "{user_name}" and password: "{user_pass}" to inputs and click LOGIN button')
def test_given_impl(context, user_name, user_pass):
    context.login_page = LoginPageModel(context.driver)
    if user_name != 'None':
        context.login_page.set_credentials_to_inputs(user_name, user_pass)
    else:
        context.login_page.login_button.click()


@then('system reveal input validations error message : "{error_message}"')
def test_step_impsl(context, error_message):
    error_validation_message = context.login_page.error_header.text
    assert error_validation_message == error_message
    # assert context.driver.current_url == 'https://www.saucedemo.com/'
