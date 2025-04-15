from playwright.sync_api import sync_playwright


def test_filter():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://todomvc.com/examples/react/dist/#")
        page.locator(".new-todo").click()
        page.locator(".new-todo").fill("Buy milk")
        page.locator(".new-todo").press("Enter")
        assert page.locator(
            ".todo-list li").nth(0).text_content() == "Buy milk"
