Feature: Log in to app as standard user


  Scenario: Log in to app as standard user
    Given user open https://www.saucedemo.com/
     When fill in the inputs with proper credentials
      And click LOGIN button
     Then system redirect page on https://www.saucedemo.com/inventory.html
