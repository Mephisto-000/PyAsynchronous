import json
from typing import Any
from urllib import error, request


OLLAMA_GENERATE_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "gemma4:e4b"
REQUEST_TIMEOUT_SECONDS = 120


class OllamaRequestError(RuntimeError):
    """代表呼叫 Ollama API 時發生可讀性較高的錯誤。"""


def generate_with_ollama(prompt: str) -> str:
    """使用 Ollama HTTP API 向本機 LLM 發送單次 prompt。"""
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        # gemma4:e4b 是 thinking 模型；教學範例關閉 thinking，避免可見回答是空字串。
        "think": False,
        "options": {
            # 限制輸出長度，讓新手執行範例時比較快看到結果。
            "num_predict": 160,
            "temperature": 0.2,
        },
    }

    body = json.dumps(payload).encode("utf-8")
    http_request = request.Request(
        OLLAMA_GENERATE_URL,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with request.urlopen(
            http_request,
            timeout=REQUEST_TIMEOUT_SECONDS,
        ) as response:
            response_body = response.read().decode("utf-8")
    except error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise OllamaRequestError(
            f"Ollama API 回傳 HTTP {exc.code}：{error_body}"
        ) from exc
    except error.URLError as exc:
        raise OllamaRequestError(
            "無法連線到 Ollama，請確認 Ollama 服務已啟動，"
            f"且模型 {OLLAMA_MODEL} 已安裝。"
        ) from exc

    data: dict[str, Any] = json.loads(response_body)
    content = data.get("response")

    if not isinstance(content, str):
        raise OllamaRequestError("Ollama 回應格式不符合預期，找不到 response。")

    answer = content.strip()
    if not answer:
        raise OllamaRequestError(
            "Ollama 回應為空字串。若使用 thinking 模型，請確認請求有設定 think=false。"
        )

    return answer
