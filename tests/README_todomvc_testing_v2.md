
## ✅ 任務 5：跨瀏覽器測試（Chromium / Firefox / WebKit）

### 🎯 任務目標  
使用 pytest + Playwright 撰寫可同時在多瀏覽器執行的自動化測試，驗證所有核心功能的瀏覽器兼容性。

### ✅ 成果摘要

- 使用 `@pytest.mark.parametrize(..., indirect=True)` 實現多瀏覽器參數化測試
- 將瀏覽器啟動邏輯抽離至 `conftest.py` 中的 fixture `browser_page`
- 所有核心測試（新增、完成、刪除、清除、篩選）均可執行於 Chromium、Firefox、WebKit
- 測試結構更清楚，可維護性提升，避免重複 browser 初始化程式碼

### 🧪 範例片段

```python
@pytest.mark.parametrize("browser_page", ["chromium", "firefox", "webkit"], indirect=True)
def test_add_todo(browser_page):
    page = TodoMVC(browser_page)
    page.goto("https://todomvc.com/examples/react/dist/#/")
    page.todo_create("Buy milk")
    assert page.todo_exists("Buy milk")
```

```python
# conftest.py
@pytest.fixture(scope="function")
def browser_page(request):
    browser_name = request.param
    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_name).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
```

### ✅ 補充筆記
- fixture 中參數可透過 `request.param` 取得
- `indirect=True` 可將參數套用至 fixture 而非測試函式
- 測試封裝結構支援跨瀏覽器重複利用
