# Created by korakk at 23/05/18
#Feature: Create a new auction
#  As a logged user
#  I want to create a new auction
#  so I can offer (sell) the food that I want
#
#  Background: There is a registered user
#    Given Exists a user "user1" with password "123password"
#    Given Exists a food name "Banana"
#
#  Scenario: Register auction
#    Given I login as user "mantonia" with password "123password"
#    When I create restaurant
#      | food        | start_price| description | available_time |
#      | Banana      |  22        | Awesome     |1111|
#    Then I'm viewing the details page for restaurant by "mantonia"
#      | food        | start_price| description | available_time |
#      | Banana      |  22        | Awesome     |1111|
#    And There are 1 auctions