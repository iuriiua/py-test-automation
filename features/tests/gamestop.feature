Feature: GameStop smoke test

  Scenario: Verify Auto-suggestion works
    Given Open Gamestop page
    When Search for Sta
    Then Auto-suggestion appears
    #When Search for Star Wars
    #Then Results are relevant
