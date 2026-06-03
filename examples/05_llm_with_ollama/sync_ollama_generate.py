import time

from ollama_http import OllamaRequestError, generate_with_ollama


PROMPTS = [
    "請用三句話說明 Python 同步程式的特性。",
    "請用三句話說明 Python asyncio 適合處理什麼問題。",
    "請用一句話提醒新手使用 await 時要注意什麼。",
]


def main() -> None:
    """依序呼叫本機 LLM，示範同步流程會等待每次回應完成。"""
    start_time = time.perf_counter()

    try:
        for index, prompt in enumerate(PROMPTS, start=1):
            print(f"\n第 {index} 次同步請求")
            print(f"Prompt：{prompt}")

            answer = generate_with_ollama(prompt)
            print(f"LLM 回答：{answer}")
    except OllamaRequestError as exc:
        raise SystemExit(f"呼叫 Ollama 失敗：{exc}") from exc

    elapsed_seconds = time.perf_counter() - start_time
    print(f"\n同步版本總耗時：{elapsed_seconds:.2f} 秒")


if __name__ == "__main__":
    main()
