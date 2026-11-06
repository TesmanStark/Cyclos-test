# Cyclos demo QA (Playwright + Pytest + Page Object Model)

Tests (4):
- login with valid data -> reaches dashboard
- login with invalid data -> stays on login
- login with empty data -> stays on login
- after login, "Pay user" opens the Payment to user page

Setup (once):
    pip install -r requirements.txt
    playwright install chromium firefox webkit

Credentials (PowerShell), if the defaults don't work:
    $env:CYCLOS_USER="your_username"
    $env:CYCLOS_PASS="your_password"

Run:
    pytest                 # everything, in chromium + firefox + webkit
    pytest -k firefox      # one browser only (also: -k chromium, -k webkit)
    pytest -m login        # login only
    pytest -m payment      # pay user page only
    pytest --headed        # watch the browser

Results: reports/report.html opens in your browser automatically after the run (set $env:CYCLOS_NO_OPEN="1" to stop that). Failure screenshots + traces: reports/artifacts/
