import asyncio


async def fetch_user_profile() -> dict[str, str]:
    """模擬透過 API 取得使用者資料。"""
    print("開始取得使用者資料")

    # await 會暫停目前 coroutine，並把控制權交回 event loop。
    await asyncio.sleep(1)

    print("完成取得使用者資料")
    return {"name": "Alice", "role": "learner"}


async def main() -> None:
    """示範如何等待單一 coroutine 完成。"""
    print("準備執行 coroutine")
    user_profile = await fetch_user_profile()
    print(f"取得結果：{user_profile}")


if __name__ == "__main__":
    asyncio.run(main())
