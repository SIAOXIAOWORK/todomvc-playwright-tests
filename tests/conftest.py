import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_page(request):
        browser_name = request.param
        with sync_playwright() as playwright:
            browser = getattr(playwright,browser_name).launch(headless = False)
            new_context = browser.new_context()
            new_page = new_context.new_page()
            yield new_page
            browser.close()