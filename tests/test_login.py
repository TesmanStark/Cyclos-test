import pytest
from config import VALID_USERS, INVALID_USERS
from pages.dashboard_page import DashboardPage

pytestmark = pytest.mark.login


def _expect_still_on_login(page, login_page):
    page.wait_for_timeout(2000)  # give the app a moment to respond
    assert "/ui/dashboard" not in page.url
    assert login_page.is_login_form_visible()


@pytest.mark.parametrize("user", VALID_USERS, ids=lambda u: u["label"])
def test_login_with_valid_data(page, login_page, user):
    login_page.login(user["username"], user["password"])
    assert DashboardPage(page).wait_until_loaded().is_loaded()


@pytest.mark.parametrize("user", INVALID_USERS, ids=lambda u: u["label"])
def test_login_with_invalid_data(page, login_page, user):
    login_page.login(user["username"], user["password"])
    _expect_still_on_login(page, login_page)
