class LoginPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        # open login page
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        # fill credentials and submit
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")