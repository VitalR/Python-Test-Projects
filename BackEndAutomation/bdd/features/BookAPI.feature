#  $ behave bdd/features/BookAPI.feature
#  $ behave bdd/features/BookAPI.feature --no-capture --tags=smoke

Feature: Verify if Books are added and deleted using Library API

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of response should be 201


  @library
  Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    Examples:
      |isbn  | aisle |
      | rand1| 1212  |
      | rand2| 2323  |