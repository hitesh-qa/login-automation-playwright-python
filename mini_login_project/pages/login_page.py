
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_link = "a[href='/login']"
        self.email_field = "input[data-qa='login-email']"
        self.password_field = "input[data-qa='login-password']"
        self.login_button = "button[data-qa='login-button']"
        self.error_message = "p[style='color: red;']"

    def navigate_to_login(self):
        self.page.click(self.login_link)

    def login(self, email, password):
        self.page.fill(self.email_field, email)
        self.page.fill(self.password_field,password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.inner_text(self.error_message)

#__init__ -> store all locators in one place
# navigate_to_login -> clicks login link
#login -> fills email, password and clicks login
#get_error_message -> grabs error text for negative tests