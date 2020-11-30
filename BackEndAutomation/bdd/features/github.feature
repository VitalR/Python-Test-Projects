
Feature: GitHub API Authentication

  Scenario: Session management check
    Given I have GitHub auth credentials
    When I hit get access API to GitHub
    Then status code of response should be 401
