### Created by korakk at 23/05/18
#Feature: Homepage Last Auctions Section
#  As a non-register user
#  I want to see LastAuctions section content
#  so I can see the latest available auctions
#
#  Background: Exists 1 auction
#    Given Exists a foodOffer description "Uep, com anam"
#    And Exists a food name "Banana"
#
#  Scenario: Navigate Last Auctions
#    When I want see LastAuctions section
#    Then I can see at least 1 auction
#    |start_price|actual_price|
#    |20         |20          |
