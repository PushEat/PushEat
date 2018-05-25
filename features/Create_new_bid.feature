## Created by korakk at 23/05/18
Feature: Create a new bid
  As a logged user
  I want to create a new bid on an auction
  so I can obtain the desired food

    Background: There is a registered user
    Given Exists a user "user1" with password "123password"
    And Exists a subscribed created by "user1"
      | first_name     | last_name          | age     | postal_code     |rate      |
      | Josep          | Figura             | 52       | 26000          | 20       |
    And Exists a foodOffer description "Uep, com anam"
      | start_price|actual_price| description | available_time |
      |  20        | 20        |Uep, com anam     |11:11|
    And I login as user "user1" with password "123password"

  Scenario: Create new bid
    When I want to create a new bid
      |bidder |offer |amount |
      |user1  |Banana|200    |
    Then I can see own bids
      |bidder |offer |amount |
      |user1  |Banana|200    |