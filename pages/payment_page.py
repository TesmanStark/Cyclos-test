import re
from playwright.sync_api import Page, expect
from .base_page import BasePage


class PaymentPage(BasePage):
    """Banking > Payment to user  (/ui/banking/self/payment)"""

    URL_GLOB = "**/ui/banking/self/payment**"

    def __init__(self, page: Page):
        super().__init__(page)
        self.to_user = page.get_by_placeholder("Type to search")

    def wait_until_loaded(self):
        self.page.wait_for_url(self.URL_GLOB, timeout=20_000)
        return self

    def expect_page_open(self):
        expect(self.page).to_have_url(re.compile(r"/ui/banking/self/payment"))
        expect(self.page).to_have_title(re.compile("Payment to user"))
        expect(self.to_user).to_be_visible()
