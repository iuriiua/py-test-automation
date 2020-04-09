Feature: Test for Amazon Search functionality

  Scenario: User can search for any product
    Given Open Amazon page
    When Search for shoes
    Then Search results for shoes is shown
