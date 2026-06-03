import asyncio


async def download_file(file_name: str, seconds: int) -> str:
    """模擬下載單一檔案。"""
    print(f"開始下載：{file_name}")
    await asyncio.sleep(seconds)
    print(f"完成下載：{file_name}")
    return f"{file_name} 下載完成"


async def main() -> None:
    """示範多個 task 可以在 event loop 中交錯執行。"""
    tasks = [
        asyncio.create_task(download_file("report.csv", 2)),
        asyncio.create_task(download_file("avatar.png", 1)),
    ]

    results = await asyncio.gather(*tasks)
    print("所有下載結果：", results)


if __name__ == "__main__":
    asyncio.run(main())
