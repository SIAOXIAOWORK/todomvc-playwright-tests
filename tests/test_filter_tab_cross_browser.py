from todoMVC import TodoMVC
import pytest

@pytest.mark.parametrize("browser_page",["chromium","firefox","webkit"],indirect=True)
def test_filter(browser_page):
    page = TodoMVC(browser_page)
    page.goto("https://todomvc.com/examples/react/dist/#/")
    page.todo_create("Buy milk")
    page.todo_create("Buy book")
    page.todo_create("Buy food")
    page.todo_complete("Buy milk")
    page.todo_complete("Buy food")
    page.todo_filter("Active")
    assert page.todo_list_count() == 1
    assert page.todo_is_visible("Buy book") is True
    page.todo_filter("Completed")
    assert page.todo_is_visible("Buy milk") is True
    assert page.todo_is_visible("Buy food") is True
    assert page.todo_list_count() == 2
    page.todo_filter("All")
    assert page.todo_list_count() == 3
    assert page.todo_is_visible("Buy book") is True
    assert page.todo_is_visible("Buy milk") is True
    assert page.todo_is_visible("Buy food") is True