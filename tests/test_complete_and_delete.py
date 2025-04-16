from playwright.sync_api import sync_playwright
from todoMVC import TodoMVC


def test_complete_task():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        newpage = browser.new_page()
        page = TodoMVC(newpage)
        page.goto("https://todomvc.com/examples/react/dist/#/")
        page.todo_create("Buy milk")
        page.todo_create("Buy book")
        page.todo_create("Buy food")
        page.todo_complete("Buy milk")
        page.todo_complete("Buy book")
        assert page.todo_completed("Buy milk") == True
        assert page.todo_completed("Buy book") == True
        assert page.todo_completed("Buy food") == False


def test_delete_task():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        newpage = browser.new_page()
        page = TodoMVC(newpage)
        page.goto("https://todomvc.com/examples/react/dist/#/")
        page.todo_create("Buy milk")
        page.todo_create("Buy book")
        page.todo_create("Buy food")
        page.todo_delete("Buy book")
        assert "Buy book" not in page.todo_list_allinner()


def test_clear_all_complete():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        newpage = browser.new_page()
        page = TodoMVC(newpage)
        page.goto("https://todomvc.com/examples/react/dist/#/")
        page.todo_create("Buy milk")
        page.todo_create("Buy book")
        page.todo_create("Buy food")
        page.todo_complete("Buy milk")
        page.todo_complete("Buy book")
        page.todo_clear_all_complete()
        assert "Buy milk" and "Buy book" not in page.todo_list_allinner()
        assert "Buy food" in page.todo_list_allinner()
