### Created by korakk at 23/05/18
#Feature: Check my rate (stars)
#  As a logged user
#  I want to check my rate
#  so I can see my popularity level
#    Background: See my rate
#    Given Exists a user "user1" with password "123password"
#      And Exists a subscribed created by "user1"
#      | first_name     | last_name          | age     | postal_code     |rate      |
#      | Josep          | Figura             | 52       | 26000          | 20       |
#    And I login as user "user1" with password "123password"
#
#  Scenario: Check my rating(about)
#    When I check about my info
#    Then I will see my rate
#      | rate |
#      | 20   |
