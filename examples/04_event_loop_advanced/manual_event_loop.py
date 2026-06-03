import asyncio


async def wait_for_service(service_name: str, seconds: int) -> str:
    """模擬等待外部服務回應。"""
    print(f"等待服務回應：{service_name}")
    await asyncio.sleep(seconds)
    print(f"服務已回應：{service_name}")
    return f"{service_name} ready"


async def main() -> None:
    """示範手動 event loop 也可以排程多個 task。"""
    results = await asyncio.gather(
        wait_for_service("payment-api", 2),
        wait_for_service("audit-log", 1),
    )
    print("服務檢查結果：", results)


if __name__ == "__main__":
    # 一般應用程式建議使用 asyncio.run()；這裡是為了理解 event loop。
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
