# Created by korakk at 23/05/18
Feature: Create a new auction
  As a logged user
  I want to create a new auction
  so I can offer (sell) the food that I want

  Background: There is a registered user
    Given Exists a user "mantonia" with password "123password"

  Scenario: Register just auction food name
    Given I login as user "mantonia" with password "123password"
    When I create restaurant
      | food        |
      | Banana      |
    Then I'm viewing the details page for restaurant by "user"
      | food        |
      | Banana      |
    And There are 1 auctions