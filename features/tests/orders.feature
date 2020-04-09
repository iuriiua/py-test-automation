Feature: Test for Orders functionality

  Scenario: Logged out user sees sign in page
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign in page is opened
