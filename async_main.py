import time
import asyncio

"""
模擬一個異步的圖像處理任務，這個任務會花費一些時間來完成。
每次處理多張圖片，直到所有圖片都處理完畢。
這種方式可以顯著減少整體處理時間，因為多張圖片的處理可以同時進行。

異步處理的優點： 
1. 提高資源利用率：在等待 I/O 操作時，CPU 可以繼續處理其他任務
2. 增強併發能力：可以同時處理多個請求
3. 改善用戶體驗：響應時間短，特別是在高負載情況下
"""

async def process_image_async(image):
    """Simulate a time-consuming image processing task."""
    print(f"Processing image: {image}")
    await asyncio.sleep(2)  # Simulate time-consuming processing
    print(f"Finished processing image: {image}")
    return f"Processed {image}"

async def main_async():
    start_time = time.time()

    images = ["image1.jpg", "image2.jpg", "image3.jpg"]
    tasks = [process_image_async(image) for image in images]
    results = await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Processed {len(images)} images in {end_time - start_time:.2f} seconds")
    print("Results:", results)

if __name__ == "__main__":
    asyncio.run(main_async())
