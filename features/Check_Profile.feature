## Created by korakk at 23/05/18
#Feature: Check my profile
#  As a logged user
#  I want to check my profile
#  so I can see my profile characteristics
#  Background: Users must exists
#    Given Exists a user "user1" with password "123password"
#    And Exists a user "user2" with password "123password"
#    And Exists a user "user3" with password "123password"
#    And Exists a subscribed created by "user1"
#      | first_name     | last_name          | age     | postal_code     |rate      |
#      | Josep          | Figura             | 52       | 26000          | 20       |
#
#    And Exists a subscribed created by "user2"
#      | first_name     | last_name          | age     | postal_code     |rate      |
#      | Maria          | Antonia            | 52       | 26000          | 5       |
#    And Exists a subscribed created by "user3"
#      | first_name     | last_name          | age     | postal_code     |rate      |
#      | Rhydon          | Roca              | 21       | 26000          | 3       |
#
#  Scenario: Check top profiles
#    When I check top profiles
#    Then I will see all top profiles including
#      | first_name     | last_name          |
#      | Josep          | Figura             |
#      | Maria          | Antonia             |
#      | Rhydon         | Roca             |