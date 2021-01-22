Feature: Log in to app with proper user

  Scenario Outline: Log in to app as all type of users
    Given user open https://www.saucedemo.com/
    When set username: "<user_name>" and password: "<user_pass>" to inputs and click LOGIN button
    Then system redirect page on https://www.saucedemo.com/inventory.html

    Examples: User types
      | user_name               | user_pass    |
      | standard_user           | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |