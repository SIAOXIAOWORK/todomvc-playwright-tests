class TodoMVC():
    def __init__(self, page):
        self.page = page

    def goto(self, URL):
        self.page.goto(URL)

    def todo_create(self, todo):
        self.page.locator(".new-todo").click()
        self.page.locator(".new-todo").fill(todo)
        self.page.locator(".new-todo").press("Enter")

    def todo_text(self, num):
        return self.page.locator(".todo-list li").nth(num).text_content()

    def todo_complete(self, todo):
        self.page.locator(
            ".todo-list li", has_text=todo).locator(".toggle").check()

    def todo_completed(self, todo):
        return self.page.locator(".todo-list li", has_text=todo).locator(".toggle").is_checked()

    def todo_delete(self, todo):
        self.page.locator(".todo-list li", has_text=todo).hover()
        self.page.locator(
            ".todo-list li", has_text=todo).locator(".destroy").click()

    def todo_list_allinner(self):
        return self.page.locator(".todo-list li").all_inner_texts()

    def todo_clear_all_complete(self):
        self.page.locator(".clear-completed").click()

    def todo_filter(self, filter):
        self.page.locator(".filters li").get_by_text(filter).click()

    def todo_list_count(self):
        return self.page.locator(".todo-list li").count()
    
    def todo_is_visible(self,todo: str) -> bool :
        return self.page.locator(".todo-list li", has_text=todo).is_visible()
    
    def todo_exists(self, todo : str) -> bool :
        return todo in [item.strip() for item in self.todo_list_allinner()]
