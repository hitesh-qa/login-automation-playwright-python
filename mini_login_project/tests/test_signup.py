import pytest
from mini_login_project.pages.signup_page import SignupPage

def test_valid_signup(page):
    signup = SignupPage(page)
    signup.navigate_to_signup()
    signup.enter_signup_details(
        "TestUser123",
        "testuser123unique@gmail.com"
    )
    signup.fill_account_info("Test@1234")
    result = signup.is_account_created()
    assert "ACCOUNT CREATED!" in result

def test_signup_existing_email(page):
    signup = SignupPage(page)
    signup.navigate_to_signup()
    signup.enter_signup_details(
        "TestUser",
        "nnero403@gmail.com"
    )
    error = signup.get_error_message()
    assert "Email Address already exist!" in error

# test_valid_signup -> registers a new unique email
# test_signup_existing_email -> tries your already registered email and expects error