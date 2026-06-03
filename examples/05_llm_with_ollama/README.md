# 05. 使用本機 Ollama 呼叫 LLM

這個章節參考「比較同步與非同步 OpenAI 用戶端」的範例，但改成使用本機 Ollama 與已安裝的 `gemma4:e4b` 模型。

本章不需要 OpenAI API key，也不新增 Python dependency。

## 前置需求

請先確認 Ollama 服務已啟動，並且本機已有 `gemma4:e4b`：

```bash
ollama list
```

如果模型不存在，可以自行安裝：

```bash
ollama pull gemma4:e4b
```

## 執行同步範例

```bash
uv run python examples/05_llm_with_ollama/sync_ollama_generate.py
```

同步版本會依序送出 prompt，每一次都要等 LLM 回應完成後，才會送出下一次請求。

## 執行非同步範例

```bash
uv run python examples/05_llm_with_ollama/async_ollama_generate.py
```

Python 標準庫沒有內建 async HTTP client。為了不新增 dependency，這個範例使用 `asyncio.to_thread()` 把阻塞式 HTTP 呼叫放到背景 thread 執行，讓 event loop 不會被卡住。

如果 production 系統需要大量 LLM 請求，可以考慮改用支援 async 的 HTTP client 或 Ollama Python client，並補上 timeout、retry、rate limit、observability 與 fallback strategy。

## 模型設定

`gemma4:e4b` 是 thinking 模型。為了讓新手範例可以直接看到回答，HTTP payload 會設定 `think: false`。

如果沒有關閉 thinking，模型可能會先產生 hidden reasoning，導致 `/api/generate` 的 `response` 暫時是空字串。

## 學習重點

- LLM API 呼叫通常是 I/O-bound 工作，適合放入非同步流程。
- 非同步可以改善等待期間的應用程式反應能力，但不保證模型推論本身變快。
- 本機 LLM 的 latency 會受到硬體、模型大小、context 長度與 Ollama 排程影響。
- prompt 應集中管理，避免散落在程式各處造成維護困難。

## 疑難排解

如果執行時看到 `llama-server binary not found`，代表 Ollama 服務有啟動，但目前的 Ollama 安裝缺少推論需要的 server binary。

這不是 Python 範例程式的錯誤，請先重新安裝或更新 Ollama，再重新執行範例。
