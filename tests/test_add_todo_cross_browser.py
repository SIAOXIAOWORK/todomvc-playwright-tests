from todoMVC import TodoMVC
import pytest

@pytest.mark.parametrize("browser_page",["chromium" , "firefox" , "webkit"],indirect=True)
def test_add_todo(browser_page):
        page = TodoMVC(browser_page)
        page.goto("https://todomvc.com/examples/react/dist/#/")
        page.todo_create("Buy book")
        page.todo_create("Buy food")
        page.todo_create("Buy milk")
        assert page.todo_text(2) == "Buy milk"
        assert page.todo_text(0) == "Buy book"
        assert page.todo_text(1) == "Buy food"
