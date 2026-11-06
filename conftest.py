import pytest
from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "base_url": BASE_URL, "viewport": {"width": 1366, "height": 768}}


@pytest.fixture
def login_page(page):
    return LoginPage(page).open()


@pytest.fixture
def dashboard(page):
    LoginPage(page).open().login(USERNAME, PASSWORD)
    return DashboardPage(page).wait_until_loaded()


def pytest_unconfigure(config):
    """After the run, open reports/report.html in the browser automatically.

    Turn off with:  $env:CYCLOS_NO_OPEN="1"
    """
    import os
    import pathlib
    import webbrowser

    if os.getenv("CYCLOS_NO_OPEN") or config.option.collectonly:
        return
    report = pathlib.Path(__file__).resolve().parent / "reports" / "report.html"
    if report.exists():
        webbrowser.open(report.as_uri())
