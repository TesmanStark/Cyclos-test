import pytest

pytestmark = pytest.mark.payment


def test_pay_user_page_opens(dashboard):
    """After login, clicking 'Pay user' opens the Payment to user page."""
    payment = dashboard.open_pay_user()
    payment.expect_page_open()
