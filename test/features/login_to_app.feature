Feature: Log in to app as standard user


  Scenario Outline: Log in to app as standard user
    Given user open "<log_in_page>"
    When set username: "<user_name>" and password: "<user_pass>" to inputs
    And click LOGIN button
    Then system redirect page on "<invetory_page>"

    Examples: Data
      | log_in_page                | invetory_page                            | user_name     | user_pass    |
      | https://www.saucedemo.com/ | https://www.saucedemo.com/inventory.html | standard_user | secret_sauce |


