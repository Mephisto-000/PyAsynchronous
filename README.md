# PyAsynchronous

這是一份給 Python 初學者閱讀的同步與非同步學習筆記。

專案用簡短、可直接執行的範例說明：

- 同步程式為什麼會等待
- `async` / `await` 如何讓程式在等待 I/O 時切換工作
- coroutine、task、event loop 之間的基本關係
- 什麼情境適合使用 `asyncio`

## 適合讀者

- 剛開始學 Python 非同步程式設計的人
- 已經會寫一般同步 Python，但不熟悉 `asyncio` 的人
- 想用實際執行時間比較同步與非同步差異的人

這份筆記不會一開始就深入多執行緒、多程序或底層 event loop 實作，而是先建立清楚的閱讀順序。

## 環境需求

本專案保留目前設定，使用 Python `3.14`。

建議使用 `uv` 執行範例：

```bash
uv run python examples/01_sync_vs_async/sync_image_processing.py
```

如果是第一次執行，`uv` 會依照專案設定建立虛擬環境。

## 建議閱讀順序

### 1. 同步與非同步的時間差

先執行同步版本：

```bash
uv run python examples/01_sync_vs_async/sync_image_processing.py
```

再執行非同步版本：

```bash
uv run python examples/01_sync_vs_async/async_image_processing.py
```

觀察重點：

- 同步版本一次只處理一張圖片，總時間約 6 秒。
- 非同步版本可以在等待時切換到其他 task，總時間約 2 秒。
- 這裡用 `sleep` 模擬 I/O-bound 工作，例如讀檔、呼叫 API、等待資料庫回應。

### 2. coroutine 基礎

```bash
uv run python examples/02_coroutine_basics/single_coroutine.py
```

觀察重點：

- `async def` 會定義 coroutine function。
- 呼叫 coroutine function 會得到 coroutine object，不會立刻執行內容。
- `await` 會等待 coroutine 完成，並在等待期間把控制權交回 event loop。
- `asyncio.run()` 是執行非同步程式最常用的入口。

### 3. 同時執行多個 task

```bash
uv run python examples/03_concurrent_tasks/multiple_tasks.py
```

觀察重點：

- `asyncio.create_task()` 會把 coroutine 排入 event loop。
- 多個 task 可以交錯執行，不需要一個完成後才開始下一個。
- 等待時間較短的 task 會先完成。

### 4. 進階補充：手動管理 event loop

```bash
uv run python examples/04_event_loop_advanced/manual_event_loop.py
```

觀察重點：

- 平常應優先使用 `asyncio.run()`。
- 手動建立 event loop 是較底層的寫法，適合理解 `asyncio.run()` 背後做了什麼。
- 新手不需要在一般應用程式中優先使用這種寫法。

### 5. LLM 呼叫：使用本機 Ollama

先確認本機已啟動 Ollama，並且已安裝 `gemma4:e4b`：

```bash
ollama list
```

執行同步版本：

```bash
uv run python examples/05_llm_with_ollama/sync_ollama_generate.py
```

再執行非同步版本：

```bash
uv run python examples/05_llm_with_ollama/async_ollama_generate.py
```

觀察重點：

- 同步版本會依序等待每一次 LLM 回應。
- 非同步版本用 `asyncio.to_thread()` 將阻塞式 HTTP 呼叫移到背景 thread，避免阻塞 event loop。
- 本章使用 Ollama HTTP API，不需要 OpenAI API key，也不新增 Python dependency。
- 因為本機 LLM 推論會受模型大小、硬體與 Ollama 排程影響，非同步版本不一定會讓推論本身變快，但可以避免應用程式在等待時完全卡住。

## 常見誤解

### `async` 不等於多執行緒

`asyncio` 的核心是 cooperative concurrency。程式必須在 `await` 時主動讓出控制權，event loop 才能切換去執行其他 task。

### `await` 不是讓程式變快的魔法

`await` 適合等待 I/O-bound 工作，例如網路請求、資料庫查詢、檔案 I/O。若工作本身是大量 CPU 計算，單靠 `asyncio` 通常不會變快。

### CPU-bound 工作不適合只靠 `asyncio`

如果任務是影像轉檔、資料壓縮、大量數學運算等 CPU-bound 工作，應考慮 multiprocessing、thread pool、process pool，或其他專門的計算架構。

## 專案結構

```text
.
├── README.md
├── main.py
├── examples/
│   ├── 01_sync_vs_async/
│   │   ├── sync_image_processing.py
│   │   └── async_image_processing.py
│   ├── 02_coroutine_basics/
│   │   └── single_coroutine.py
│   ├── 03_concurrent_tasks/
│   │   └── multiple_tasks.py
│   ├── 04_event_loop_advanced/
│   │   └── manual_event_loop.py
│   └── 05_llm_with_ollama/
│       ├── README.md
│       ├── ollama_http.py
│       ├── sync_ollama_generate.py
│       └── async_ollama_generate.py
├── pyproject.toml
└── uv.lock
```

## 參考資料

- [iThome 鐵人賽目錄](https://ithelp.ithome.com.tw/m/users/20162280/ironman/8477)
- [同步與非同步](https://ithelp.ithome.com.tw/m/articles/10381611)
- [事件迴圈](https://ithelp.ithome.com.tw/articles/10199408)
