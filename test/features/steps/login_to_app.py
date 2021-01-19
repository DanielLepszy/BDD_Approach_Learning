from behave import given, when, then

# from BDD_Approach_Learning.test.features.login_page import LoginPageModel
from page_models.page_models_factory.pages.login_page.login_page import LoginPageModel


@given('user open "{log_in_page}"')
def test_given_impl(context, log_in_page):
    context.driver.get(log_in_page)
    # home = HomeModel(context)


@when('set username: "{user_name}" and password: "{user_pass}" to inputs')
def test_given_impl(context, user_name, user_pass):
    page = LoginPageModel(context.driver).set_credentials_to_inputs(user_name, user_pass)

@when('click LOGIN button')
def test_when_impl(context):  # -- NOTE: number is converted into integer
    assert True
    # assert number > 1 or number == 0
    # context.tests_count = number


@then('system redirect page on "{invetory_page}"')
def test_step_impsl(context, invetory_page):
    assert True
