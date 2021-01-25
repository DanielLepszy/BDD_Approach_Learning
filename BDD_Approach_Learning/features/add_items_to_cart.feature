Feature: Inventory user action

  @add_items_to_cart
  Scenario: Add items to cart and check shopping list properity
    Given user log in to app using specified credentials: standard_user and secret_sauce
    When user add selected items to cart
      | item title            |
      | Sauce Labs Backpack   |
      | Sauce Labs Bike Light |
    And click in shopping trolley icon to open cart
    Then user cart contains previous added items
      | item title            |
      | Sauce Labs Backpack   |
      | Sauce Labs Bike Light |
