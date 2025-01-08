Feature: Validate Coindesk API response

  Scenario: Verify response contains specific BPIs and GBP description
    Given the user sends a GET request to "https://api.coindesk.com/v1/bpi/currentprice.json"
    Then the response contains exactly 3 BPIs
    And the response contains BPIs "USD", "GBP", and "EUR"
    And the GBP description equals "British Pound Sterling"
