Feature: Subscription Management

  Scenario: Create Base Subscription
    Given the user collects the base subscription details
    When the user tries to create a new subscription
    Then the new subscription should be created with a response status code of 200
    And the subscription name in the response should match the given payload
