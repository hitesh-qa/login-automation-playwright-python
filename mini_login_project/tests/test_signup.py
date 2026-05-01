import pytest
from pages.signup_page import SignupPage
import time
def generate_email():
    return f"testuser{int(time.time())}@test.com"

def test_valid_signup(page):
    signup = SignupPage(page)
    signup.navigate_to_signup_page()
    signup.enter_signup_details(
        "TestUser123",
        generate_email()
    )
    signup.fill_account_info("Test@1234")
    result = signup.is_account_created()
    assert "account_created" in result

def test_signup_existing_email(page):
    signup = SignupPage(page)
    signup.navigate_to_signup_page()
    signup.enter_signup_details(
        "TestUser",
        "nnero403@gmail.com"
    )
    error = signup.get_error_message()
    assert "Email Address already exist!" in error

# test_valid_signup -> registers a new unique email
# test_signup_existing_email -> tries your already registered email and expects error