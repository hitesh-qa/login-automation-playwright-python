import pytest
import csv
from pages.login_page import LoginPage

def load_login_data():
    test_data = []
    with open("test_data/login_data.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            test_data.append((row["email"],
                              row["password"],
                              row["expected_result"]))
    return test_data
@pytest.mark.parametrize("email,password,expected", load_login_data())
def test_login(page, email, password, expected):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login(email, password)

    if expected == "success":
        assert "Logged in as" in page.inner_text("body")
    else:
        try:
            error = login.get_error_message()
            assert "inncorrect" in error or error == ""
        except:
            assert page.url =="https://www.automationexercise.com/login"

# load_login_data -> reads all rows from CSV
# @pytest.mark.parametrize -> runs test once for each row automatically
# if expected == "success" -> checks page title after valid login
# else -> checks error message for all failure cases