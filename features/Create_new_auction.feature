## Created by korakk at 23/05/18
Feature: Create a new auction
  As a logged user
  I want to create a new auction
  so I can offer (sell) the food that I want

  Background: There is a registered user
    Given Exists a user "user1" with password "123password"
    And Exists a subscribed created by "user1"
      | first_name     | last_name          | age     | postal_code     |rate      |
      | Josep          | Figura             | 52       | 26000          | 20       |
    And Exists a food name "Banana"
    And I login as user "user1" with password "123password"

  Scenario: Create auction
    When I create a new auction
      | start_price|actual_price| description | available_time |
      |  20        | 20        |Uep, com anam     |11:11|
    Then I'm viewing the details of the auction
      | start_price|actual_price| description | available_time |
      |  20        | 20         |Uep, com anam     |11:11|