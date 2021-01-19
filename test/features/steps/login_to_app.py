from behave import given, when, then
from selenium import webdriver

from BDD_Approach_Learning.test.code.home_model import HomeModel


@given('user open https://www.saucedemo.com/')
def test_given_impl(context):
    context.driver.get("https://www.saucedemo.com")
    home = HomeModel(context)

@when('fill in the inputs with proper credentials')
def test_given_impl(context):
    print('xx')

@when('click LOGIN button')
def test_when_impl(context):  # -- NOTE: number is converted into integer
    assert True
    # assert number > 1 or number == 0
    # context.tests_count = number

@then('system redirect page on https://www.saucedemo.com/inventory.html')
def test_step_impsl(context):
    assert True
