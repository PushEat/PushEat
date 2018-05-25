# Created by korakk at 25/05/18
Feature: Create a new bid
  As a logged user
  I want to create a new food
  so I can create the desired food
    Background: See my rate
    Given Exists a user "user1" with password "123password"
      And Exists a subscribed created by "user1"
      | first_name     | last_name          | age     | postal_code     |rate      |
      | Josep          | Figura             | 52       | 26000          | 20       |
    And I login as user "user1" with password "123password"

  Scenario:
    When I search de navbar food button
    Then I create a food
      | type      | name          | calories     | fats     |proteins      |
      | Main Dish | Tomato        | 52           | 70       | 20           |
    Then I create a food with his characteristics
      | type      | name          | calories     | fats     |proteins      |
      | Main Dish | Tomato        | 52           | 70       | 20           |