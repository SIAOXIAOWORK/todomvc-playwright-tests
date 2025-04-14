from playwright.sync_api import sync_playwright

def test_add_task():
     with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://todomvc.com/examples/react/dist/#/")
        page.locator(".new-todo").click()
        page.locator(".new-todo").fill("Buy milk")
        page.locator(".new-todo").press("Enter")
        page.locator(".new-todo").click()
        page.locator(".new-todo").fill("Buy Food")
        page.locator(".new-todo").press("Enter")
        page.locator(".new-todo").click()
        page.locator(".new-todo").fill("Buy Book")
        page.locator(".new-todo").press("Enter")
        page.locator(".toggle").nth(0).click()
        page.locator(".toggle").nth(1).click()
        page.locator(".todo-list li").nth(0).hover()
        page.locator(".todo-list li .destroy").nth(0).click()
        assert page.locator(".todo-list li").nth(0).text_content() == "Buy Food"
        page.locator(".clear-completed").click()
        assert page.locator(".todo-list li").nth(0).text_content() == "Buy Book"

