Feature: Remove all items from user cart

  Scenario: Remove all added items from user cart and continue shopping
    Given standard user log in to app
    When user add whole items to cart
      | item title                               |
      | Sauce Labs Backpack                      |
      | Sauce Labs Bike Light                    |
      | Sauce Labs Sauce Labs Bolt T-Shirt Light |
      | Sauce Labs Fleece Jacket                 |
      | Sauce Labs Bike Sauce Labs Onesie        |
      | Test.allTheThings() T-Shirt (Red)        |
    And click in shopping trolley icon
    And remove all items from cart
      | item title                               |
      | Sauce Labs Backpack                      |
      | Sauce Labs Bike Light                    |
      | Sauce Labs Sauce Labs Bolt T-Shirt Light |
      | Sauce Labs Fleece Jacket                 |
      | Sauce Labs Bike Sauce Labs Onesie        |
      | Test.allTheThings() T-Shirt (Red)        |
    Then click CONTINUE SHOPPING button
    And check if items are able to add again to cart
      | item title                               |
      | Sauce Labs Backpack                      |
      | Sauce Labs Bike Light                    |
      | Sauce Labs Sauce Labs Bolt T-Shirt Light |
      | Sauce Labs Fleece Jacket                 |
      | Sauce Labs Bike Sauce Labs Onesie        |
      | Test.allTheThings() T-Shirt (Red)        |
