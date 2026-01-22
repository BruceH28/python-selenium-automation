
Feature: Test for Target Search

  Scenario: User can search for a product on Target
    Given Open target main page
    When Click VA HEALTH CONSENT button
    And Search for beyblade x
    Then Verify search worked


  Scenario: Verify users cart is Empty
    Given Open target main page
    When Click VA HEALTH CONSENT button
    And Click on Cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Logged out User can navigate to Sign In
    Given Open target main page
    When Click VA HEALTH CONSENT button
    And Click on Account icon
    And Click on Sign in button
    Then Verify 'Sign in or create account' is shown
