Feature: Inventory user action

  Scenario: Try to
    Given user log in to app using specified credentials: standard_user and secret_sauce
    When user add selected items to cart
      | item title            |
      | Sauce Labs Backpack   |
      | Sauce Labs Bike Light |
    And click in shopping trolley icon to open cart
    Then user cart contain previous added items
      | item title            |
      | Sauce Labs Backpack   |
      | Sauce Labs Bike Light |
