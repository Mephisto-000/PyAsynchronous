import asyncio

async def my_coroutine():
    print("Hello from the coroutine!")
    await asyncio.sleep(1)  # Simulate some asynchronous work
    print("Coroutine has finished its work.")

async def main():
    print("Starting the coroutine.")
    await my_coroutine()
    print("Coroutine has finished.")


if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine