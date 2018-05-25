## Created by korakk at 23/05/18
Feature: Rate other users
  As a logged user
  I want rate other users
  so I can gave them feedback

  Background: Logged User
    Given Exists a user "user1" with password "123password"
    And Exists a subscribed created by "user1"
    | first_name     | last_name          | age     | postal_code     |rate      |
    | Josep          | Figura             | 52       | 26000          | 20       |
    And I login as user "user1" with password "123password"

  Scenario: Rate user
    When I login as user "user1" with password "123password"
    Then I rate up a user