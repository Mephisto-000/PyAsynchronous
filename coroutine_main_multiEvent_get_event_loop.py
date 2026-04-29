import asyncio


async def my_coroutine_1():
    print("Start example 1 coroutine.")
    await asyncio.sleep(2)  # Simulate some asynchronous work
    print("Example 1 coroutine has finished.")


async def my_coroutine_2():
    print("Start example 2 coroutine.")
    await asyncio.sleep(1)  # Simulate some asynchronous work
    print("Example 2 coroutine has finished.")


async def main(loop):
    tasks = [
        loop.create_task(my_coroutine_1()),
        loop.create_task(my_coroutine_2()),
    ]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        current_loop = asyncio.get_event_loop()
        current_loop.run_until_complete(main(current_loop))
    finally:
        current_loop.close()