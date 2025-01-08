import requests
from behave import given, then

#  Send a GET request to the Coindesk API
@given('the user sends a GET request to "{url}"')
def send_get_request(context, url):
    # Send GET request to the provided URL
    response = requests.get(url)
    context.response = response
    context.response_data = response.json()  

#   Verify that the response contains exactly 3 BPIs
@then('the response contains exactly 3 BPIs')
def verify_number_of_bpis(context):
    # Extract the 'bpi' section from the response data
    bpi = context.response_data.get("bpi", {})
    assert len(bpi) == 3, f"Expected 3 BPIs, but found {len(bpi)}"

# Verify that the response contains BPIs "USD", "GBP", and "EUR"
@then('the response contains BPIs "{bpi1}", "{bpi2}", and "{bpi3}"')
def verify_bpi_keys(context, bpi1, bpi2, bpi3):
    # Extract the 'bpi' keys
    bpi = context.response_data.get("bpi", {})
    keys = bpi.keys()
    assert bpi1 in keys, f"{bpi1} not found in BPIs"
    assert bpi2 in keys, f"{bpi2} not found in BPIs"
    assert bpi3 in keys, f"{bpi3} not found in BPIs"

# Verify that the GBP description equals "British Pound Sterling"
@then('the GBP description equals "{expected_description}"')
def verify_gbp_description(context, expected_description):
    # Get the GBP description from the response data
    gbp = context.response_data.get("bpi", {}).get("GBP", {})
    description = gbp.get("description", "")
    assert description == expected_description, (
        f"Expected GBP description to be '{expected_description}', "
        f"but got '{description}'"
    )
