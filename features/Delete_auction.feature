## Created by korakk at 23/05/18
Feature: Delete an auction
  As a logged user
  I want to delete an auction
  so I can remove it
  Background: Auction created

    Given Exists a user "user1" with password "123password"
    And Exists a subscribed created by "user1"
      | first_name     | last_name          | age     | postal_code     |rate      |
      | Josep          | Figura             | 52       | 26000          | 20       |
    And I login as user "user1" with password "123password"
    And Exists a foodOffer description "Uep, com anam"
      | start_price|actual_price| description | available_time |
      |  20        | 20        |Uep, com anam     |11:11|
    And Exists a food name "Banana"


  Scenario:  Delete Auction
    When I want to delete an auction I click the delete button
