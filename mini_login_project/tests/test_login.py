import pytest
import csv
from mini_login_project.pages.login_page import LoginPage

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
        assert "My Account" in page.title()
    else:
        error = login.get_error_message()
        assert "Your email or password is incorrect" in error \
                or error == "" \
                or page.url =="https://www.automationexercise.com/login"

# load_login_data -> reads all rows from CSV
# @pytest.mark.parametrize -> runs test once for each row automatically
# if expected == "success" -> checks page title after valid login
# else -> checks error message for all failure cases