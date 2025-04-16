from playwright.sync_api import sync_playwright
from todoMVC import TodoMVC


def test_add_task():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_page()
        page = TodoMVC(context)
        page.goto("https://todomvc.com/examples/react/dist/#/")
        page.todo_create("Buy book")
        page.todo_create("Buy food")
        page.todo_create("Buy milk")
        assert page.todo_text(2) == "Buy milk"
        assert page.todo_text(0) == "Buy book"
        assert page.todo_text(1) == "Buy food"
        browser.close()
