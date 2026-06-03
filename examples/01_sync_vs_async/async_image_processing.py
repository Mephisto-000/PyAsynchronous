import asyncio
import time


IMAGE_PROCESSING_SECONDS = 2
IMAGE_FILES = ["image1.jpg", "image2.jpg", "image3.jpg"]


async def process_image_async(image_file: str) -> str:
    """模擬非同步處理單張圖片。"""
    print(f"開始處理圖片：{image_file}")

    # asyncio.sleep 代表正在等待一個可讓出控制權的 I/O-bound 工作。
    await asyncio.sleep(IMAGE_PROCESSING_SECONDS)

    print(f"完成處理圖片：{image_file}")
    return f"已處理 {image_file}"


async def main() -> None:
    """同時排入多個 task，示範等待期間可以切換處理其他工作。"""
    start_time = time.perf_counter()

    tasks = [process_image_async(image_file) for image_file in IMAGE_FILES]
    results = await asyncio.gather(*tasks)

    elapsed_seconds = time.perf_counter() - start_time
    print(f"共處理 {len(IMAGE_FILES)} 張圖片，耗時 {elapsed_seconds:.2f} 秒")
    print("處理結果：", results)


if __name__ == "__main__":
    asyncio.run(main())
