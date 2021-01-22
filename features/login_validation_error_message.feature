Feature: Log in to app with unpermitted user

  Scenario Outline: Try to log in to unpermitted users
    Given unpermitted user open https://www.saucedemo.com/
    When set wrong username: "<user_name>" and password: "<user_pass>" to inputs and click LOGIN button
    Then system reveal input validations error message : "<error_message>"

    Examples: User types
      | user_name            | user_pass            | error_message                                                             |
      | locked_out_user      | secret_sauce         | Epic sadface: Sorry, this user has been locked out.                       |
      | nonexistent_username | nonexistent_password | Epic sadface: Username and password do not match any user in this service |
      | None                 | None                 | Epic sadface: Username is required                                        |