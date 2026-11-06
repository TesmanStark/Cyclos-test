from playwright.sync_api import Page, expect
from .base_page import BasePage
from .payment_page import PaymentPage


class DashboardPage(BasePage):
    URL_GLOB = "**/ui/dashboard**"

    def __init__(self, page: Page):
        super().__init__(page)
        self.navigation = page.locator("[role='navigation'], nav").first

    def wait_until_loaded(self):
        self.page.wait_for_url(self.URL_GLOB, timeout=20_000)
        expect(self.page.locator("input[type='password']")).to_have_count(0)
        return self

    def is_loaded(self) -> bool:
        return "/ui/dashboard" in self.page.url

    def open_pay_user(self) -> PaymentPage:
        """Click the 'Pay user' quick-access tile on the dashboard."""
        self.page.get_by_text("Pay user", exact=True).first.click()
        return PaymentPage(self.page).wait_until_loaded()
