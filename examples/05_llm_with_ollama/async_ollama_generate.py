import asyncio
import time

from ollama_http import OllamaRequestError, generate_with_ollama


PROMPTS = [
    "請用三句話說明 Python 同步程式的特性。",
    "請用三句話說明 Python asyncio 適合處理什麼問題。",
    "請用一句話提醒新手使用 await 時要注意什麼。",
]


async def ask_llm(prompt: str) -> str:
    """將阻塞式 Ollama HTTP 呼叫移到背景 thread，避免阻塞 event loop。"""
    return await asyncio.to_thread(generate_with_ollama, prompt)


async def main() -> None:
    """同時排入多個 LLM 請求，示範非同步流程的等待方式。"""
    start_time = time.perf_counter()
    tasks = [asyncio.create_task(ask_llm(prompt)) for prompt in PROMPTS]

    try:
        answers = await asyncio.gather(*tasks)
    except OllamaRequestError as exc:
        raise SystemExit(f"呼叫 Ollama 失敗：{exc}") from exc

    for index, answer in enumerate(answers, start=1):
        print(f"\n第 {index} 次非同步請求完成")
        print(f"Prompt：{PROMPTS[index - 1]}")
        print(f"LLM 回答：{answer}")

    elapsed_seconds = time.perf_counter() - start_time
    print(f"\n非同步版本總耗時：{elapsed_seconds:.2f} 秒")


if __name__ == "__main__":
    asyncio.run(main())
