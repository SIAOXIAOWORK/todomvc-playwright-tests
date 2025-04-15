class TodoMVC():
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto("https://todomvc.com/examples/react/dist/#")

    def add_task(self, title):
        self.locator(".new-todo").click()
        self.locator(".new-todo").fill(str(title))
        self.locator(".new-todo").press("Enter")
