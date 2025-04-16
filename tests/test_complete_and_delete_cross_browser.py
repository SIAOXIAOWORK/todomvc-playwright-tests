from todoMVC import TodoMVC
import pytest

@pytest.mark.parametrize("browser_page",["chromium","firefox","webkit"],indirect = True)
def test_complete_task(browser_page):
    page = TodoMVC(browser_page)
    page.goto("https://todomvc.com/examples/react/dist/#/")
    page.todo_create("Buy milk")
    page.todo_create("Buy book")
    page.todo_create("Buy food")
    page.todo_complete("Buy milk")
    page.todo_complete("Buy book")
    assert page.todo_completed("Buy milk") 
    assert page.todo_completed("Buy book") 
    assert not page.todo_completed("Buy food") 

@pytest.mark.parametrize("browser_page",["chromium","firefox","webkit"],indirect = True)
def test_delete_task(browser_page):
    page = TodoMVC(browser_page)
    page.goto("https://todomvc.com/examples/react/dist/#/")
    page.todo_create("Buy milk")
    page.todo_create("Buy book")
    page.todo_create("Buy food")
    page.todo_delete("Buy book")
    assert not page.todo_exists("Buy book")

@pytest.mark.parametrize("browser_page",["chromium","firefox","webkit"],indirect = True)
def test_clear_all_complete(browser_page):
    page = TodoMVC(browser_page)
    page.goto("https://todomvc.com/examples/react/dist/#/")
    page.todo_create("Buy milk")
    page.todo_create("Buy book")
    page.todo_create("Buy food")
    page.todo_complete("Buy milk")
    page.todo_complete("Buy book")
    page.todo_clear_all_complete()
    assert not page.todo_exists("Buy milk")
    assert not page.todo_exists("Buy book")
    assert page.todo_exists("Buy food")
