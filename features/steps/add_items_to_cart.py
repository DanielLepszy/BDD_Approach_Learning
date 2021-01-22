from behave import given, when, then


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
    user_cart = context.page_factory.get_user_cart_page().get_item_list_model_in_cart()

