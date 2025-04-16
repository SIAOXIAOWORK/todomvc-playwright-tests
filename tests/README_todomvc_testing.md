
# 🧪 TodoMVC 自動化測試專案 (Playwright + Python + Pytest)

本專案以 [TodoMVC](https://todomvc.com/examples/react/dist/#/) 為測試目標，透過 Playwright + Pytest 撰寫自動化測試，並封裝為類別 `TodoMVC` 增加可維護性與可讀性。

---

## ✅ 專案結構

```
.
├── tests/
│   ├── test_add_todo.py              # 任務新增測試
│   ├── test_complete_and_delete.py   # 勾選完成 / 刪除任務 / 清除已完成
│   ├── test_filter_tabs.py           # 篩選功能測試（All / Active / Completed）
├── todoMVC.py                        # 封裝操作方法的核心類別
├── requirements.txt
└── README.md
```

---

## 🧩 封裝方法一覽（todoMVC.py）

| 方法 | 功能 |
|------|------|
| `todo_create(todo)` | 建立新任務 |
| `todo_text(index)` | 取得第 n 筆任務文字 |
| `todo_complete(todo)` | 勾選指定任務為完成 |
| `todo_completed(todo)` | 驗證是否已完成 |
| `todo_delete(todo)` | 刪除指定任務 |
| `todo_list_allinner()` | 回傳所有任務文字列表 |
| `todo_list_count()` | 回傳目前顯示任務數量 |
| `todo_clear_all_complete()` | 清除所有已完成任務 |
| `todo_filter("Active")` | 篩選任務頁籤 |
| `is_todo_visible(todo)` | ✅ 驗證指定任務是否在畫面上 |

---

## 🔍 技術補充筆記

### ✅ 如何顯示 pytest 中的 `print()`

```bash
pytest -s
```
使用 `-s` 避免 pytest 隱藏標準輸出

---

### ✅ `.text_content()` vs `.inner_text()` vs `.all_inner_texts()`

| 方法 | 特性 |
|------|------|
| `.inner_text()` | 快速但不穩定，元素未渲染會出錯 |
| `.text_content()` | 穩定，會等待元素渲染完成 |
| `.all_inner_texts()` | 回傳多個元素文字，適合清單比對 |

---

### ✅ `browser.new_page()` vs `browser.new_context().new_page()`

- `new_page()`：簡單快速，適合單頁操作
- `new_context()`：可獨立 cookie/session，更貼近真實使用者行為

---

### ✅ 根據任務文字勾選 checkbox

```python
self.page.locator(".todo-list li", has_text=todo).locator(".toggle").click()
```

不能對 `.toggle` 使用 `get_by_text()`，因為 checkbox 沒有文字。

---

### ✅ 判斷任務是否出現在畫面上

```python
def is_todo_visible(todo):
    return page.locator(".todo-list li", has_text=todo).count() > 0
```

- `.count() > 0`：✅ 安全、穩定，表示在 DOM 中存在
- `.is_visible()`：檢查是否可見，但找不到會拋例外

---

## 🧪 已完成任務

- [x] 任務 1：建立測試專案結構與 Git 管理
- [x] 任務 2：新增任務功能測試
- [x] 任務 3：完成/刪除/清除任務測試
- [x] 任務 4：篩選功能測試
- [ ] 任務 5：跨瀏覽器測試（即將開始）

---

## 📦 安裝與執行

```bash
# 建立虛擬環境
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 安裝瀏覽器驅動
playwright install

# 執行所有測試
pytest -s
```

---

## 👨‍💻 作者
本作品由測試工程師練習自動化封裝與測試架構設計所撰寫，適合作為 Playwright 初中階作品集。
