Feature: Inventory user action

  Scenario: Try to
    Given user log in to app using specified credentials: standard_user and secret_sauce
    When user add selected items to cart
      | Sauce Labs Backpack   |
      | Sauce Labs Bike Light |
    And click in shopping trolley icon to open cart
    Then user cart contain previous added items

#    Examples: User types
#      | user_name     | user_pass    |
#      | standard_user | secret_sauce |
