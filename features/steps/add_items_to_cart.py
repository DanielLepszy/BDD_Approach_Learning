from behave import given, when, then
from delayed_assert import delayed_assert

from BDD_Approach_Learning.core_implementation.page_models.page_models_factory.pages.cart_page.model.item_model_in_cart import ItemModelInCart


@given('user log in to app using specified credentials: standard_user and secret_sauce')
def test_given_impl(context):
    context.driver.get('https://www.saucedemo.com/')
    context.page_factory.get_login_page().set_credentials_to_inputs('standard_user', 'secret_sauce')


@when('user add selected items to cart')
def test_when_impl(context):
    items_name = []
    for row in context.table: items_name.append(row['item title'])

    context.inventory_page = context.page_factory.get_inventory_page()
    inventory_section = context.inventory_page.get_inventory_section()
    inventory_section.add_to_cart_specified_items(items_name)


@when('click in shopping trolley icon to open cart')
def test_when_impl(context):
    header_section = context.inventory_page.get_header_section()
    header_section.shopping_trolley_icon.click()


@then('user cart contain previous added items')
def test_step_impsl(context):
    items_name: list[str] = []
    for row in context.table: items_name.append(row['item title'])
    items_in_cart: list[ItemModelInCart] = context.page_factory.get_user_cart_page().get_item_list_model_in_cart()

    for item in items_in_cart:
        delayed_assert.expect(item.title.text in items_name, "Value don't match. Probably wrong items name")

    delayed_assert.assert_all()
