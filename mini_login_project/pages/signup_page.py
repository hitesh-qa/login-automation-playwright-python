class SignupPage:

    def __init__(self, page):
        self.page = page
        self.signup_name = "input[data-qa='signup-name']"
        self.signup_email = "input[data-qa='signup-email']"
        self.signup_button = "button[data-qa='signup-button']"
        self.password_field = "input[data-qa='password']"
        self.create_account_button = "button[data-qa='create-account']"
        self.account_created_text ="b"
        self.error_message ="p[style='color: red;']"

    def navigate_to_signup_page(self):
        self.page.click("a[href='/login']")

    def enter_signup_details(self, name, email):
        self.page.fill(self.signup_name, name)
        self.page.fill(self.signup_email, email)
        self.page.click(self.signup_button)

    def fill_account_info(self, password):
        self.page.click("input[id='id_gender1']")
        self.page.fill("input[id='password']", password)
        self.page.fill("input[id='first_name']", "Test")
        self.page.fill("input[id='last_name']", "User")
        self.page.fill("input[id='address1']", "123 Test Street")
        self.page.fill("input[id='state']", "Maharashtra")
        self.page.fill("input[id='city']", "Mumbai")
        self.page.fill("input[id='zipcode']", "400001")
        self.page.fill("input[id='mobile_number']", "9999999999")
        self.page.click("button[data-qa='create-account']")

    def get_error_message(self):
        return self.page.inner_text(self.error_message)

    def is_account_created(self):
        return self.page.url

# navigate_to_signup -> goes to login/signup page
# enter_signup_details -> fills name and email
# fill_account_info -> fills password and submits
#get_error_message -> for negative test cases
# is_account_created -> checks success message