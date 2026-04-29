import asyncio


async def my_coroutine_1():
    print("Start example 1 coroutine.")
    await asyncio.sleep(2)  # Simulate some asynchronous work
    print("Example 1 coroutine has finished.")

async def my_coroutine_2():
    print("Start example 2 coroutine.")
    await asyncio.sleep(1)  # Simulate some asynchronous work
    print("Example 2 coroutine has finished.")

async def main():
    tasks = [
        asyncio.create_task(my_coroutine_1()),  # Schedule the first coroutine
        asyncio.create_task(my_coroutine_2())   # Schedule the second coroutine
    ]

    await asyncio.wait(tasks)  # Run until all tasks are completed

if __name__ == "__main__":
    asyncio.run(main())
