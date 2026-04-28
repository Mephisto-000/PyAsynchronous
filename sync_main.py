import time

"""
模擬一個同步的圖像處理任務，這個任務會花費一些時間來完成。
每次處理一張圖片，直到所有圖片都處理完畢。
這種方式會導致整體處理時間較長，因為每張圖片的處理都是依次進行的。

同步處理有幾個明顯的限制：

1. 資源浪費：在等待 I/O 操作（如檔案讀取、網路請求）時，CPU 閒置
2. 低併發能力：無法同時處理多個請求
3. 用戶體驗差：響應時間長，特別是在高負載情況下
"""


def process_image_sync(image):
    """"Simulate a time-consuming image processing task."""
    print(f"Processing image: {image}")
    time.sleep(2)  # Simulate time-consuming processing
    print(f"Finished processing image: {image}")
    return f"Processed {image}"

def main_sync():
    start_time = time.time()

    images = ["image1.jpg", "image2.jpg", "image3.jpg"]
    results = []

    for image in images:
        result = process_image_sync(image)
        results.append(result)

    end_time = time.time()
    print(f"Processed {len(images)} images in {end_time - start_time:.2f} seconds")
    print("Results:", results)

if __name__ == "__main__":
    main_sync()
