## Created by korakk at 23/05/18
Feature: Check my rate (stars)
  As a logged user
  I want to check my rate
  so I can see my popularity level
    Background: See my rate
    Given Exists a user "user1" with password "123password"
    Given I login as user "user1" with password "123password"

  Scenario: Check my rating(about)
    When I check about my info
    Then I will see my rate
      | first_name     | last_name          | rate |
      | Maria          | Antonia            | 5   |
