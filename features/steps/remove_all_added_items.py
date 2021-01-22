from behave import given, when, then
from delayed_assert import delayed_assert

from core_implementation.page_models.page_models_factory.pages.cart_page.model.item_model_in_cart import ItemModelInCart
from core_implementation.page_models.page_models_factory.pages.inventory_page.sections.model.card_model import \
    InventoryCardModel


@given('standard user log in to app')
def test_given_impl(context):
    context.driver.get('https://www.saucedemo.com/')
    context.page_factory.get_login_page().set_credentials_to_inputs('standard_user', 'secret_sauce')


@when('user add whole items to cart')
def test_when_impl(context):
    items_name = []
    for row in context.table: items_name.append(row['item title'])

    context.inventory_page = context.page_factory.get_inventory_page()
    context.inventory_section = context.inventory_page.get_inventory_section()
    context.inventory_section.add_to_cart_specified_items(items_name)


@when('click in shopping trolley icon')
def test_when_impl(context):
    header_section = context.inventory_page.get_header_section()
    header_section.shopping_trolley_icon.click()


@when('remove all items from cart')
def test_step_impsl(context):
    items_name: list[str] = []
    for row in context.table: items_name.append(row['item title'])
    context.user_cart_page = context.page_factory.get_user_cart_page()
    items_in_cart: list[ItemModelInCart] = context.user_cart_page.get_item_list_model_in_cart()

    for item in items_in_cart:
        if item.title.text in items_name:
            item.remove_btn.click()


@then("click CONTINUE SHOPPING button")
def test_continue_shopping(context):
    context.user_cart_page.continue_shopping_button.click()
    assert context.driver.current_url == 'https://www.saucedemo.com/inventory.html'


@then("check if items are able to add again to cart")
def test_button_availability(context):
    items_name: list[str] = []
    for row in context.table: items_name.append(row['item title'])
    inventory_elements: list[InventoryCardModel] = context.inventory_section.get_card_item_elements()

    for inv_element in inventory_elements:
        if inv_element.item_title.text in items_name:
            delayed_assert.expect(inv_element.add_card_button.is_displayed())

    delayed_assert.assert_expectations()
