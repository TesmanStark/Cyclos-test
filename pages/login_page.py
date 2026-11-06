from playwright.sync_api import Page, TimeoutError as PWTimeout
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PATH = "/ui/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.password = page.locator("input[type='password']")
        self.username = page.locator(
            "input:not([type='password']):not([type='hidden']):not([type='checkbox'])"
        ).first

    def open(self):
        # The Angular UI can bootstrap slowly on a cold start. Wait for the
        # form; if it never renders, reload once and wait again.
        self.page.goto(self.LOGIN_PATH, wait_until="domcontentloaded")
        try:
            self.password.wait_for(state="visible", timeout=15_000)
        except PWTimeout:
            self.page.reload(wait_until="domcontentloaded")
            self.password.wait_for(state="visible", timeout=20_000)
        return self

    def login(self, user: str, password: str):
        self.username.fill(user)
        self.password.fill(password)
        # Enter submits the form without depending on the button's label.
        self.password.press("Enter")

    def is_login_form_visible(self) -> bool:
        return self.password.is_visible()
