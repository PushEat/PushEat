### Created by korakk at 23/05/18
#Feature: Homepage Popular Users Section
#  As a non-register user
#  I want to see PopularUsers section content
#  so I can see the top rated users
#
#  Background: Registered user must exist
#    Given Exists a user "user1" with password "123password"
#    And Exists a subscribed created by "user1"
#      | first_name     | last_name          | age     | postal_code     |rate      |
#      | Josep          | Figura             | 52       | 26000          | 20       |
#  Scenario: Navigate Popular Users
#    When I want too see PopularUsers section
#    Then I can see 1 top rated user
#    |first_name|last_name|
#    |Josep     |Figura   |