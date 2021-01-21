Feature: Inventory user action

  Scenario Outline: Try to
    Given user log in to app using specified credentials: "<user_name>" and "<user_pass>u
    When user add selected items to cart
      | Sauce Labs Backpack   |
      | Sauce Labs Bike Light |
    And click in shopping trolley icon to open cart
    Then user cart contain previous added items

    Examples: User types
      | user_name     | user_pass    |
      | standard_user | secret_sauce |
