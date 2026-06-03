import time


IMAGE_PROCESSING_SECONDS = 2
IMAGE_FILES = ["image1.jpg", "image2.jpg", "image3.jpg"]


def process_image_sync(image_file: str) -> str:
    """模擬同步處理單張圖片。"""
    print(f"開始處理圖片：{image_file}")

    # time.sleep 代表正在等待一個阻塞式 I/O-bound 工作完成。
    time.sleep(IMAGE_PROCESSING_SECONDS)

    print(f"完成處理圖片：{image_file}")
    return f"已處理 {image_file}"


def main() -> None:
    """依序處理圖片，示範同步程式會逐一等待每個工作完成。"""
    start_time = time.perf_counter()
    results: list[str] = []

    for image_file in IMAGE_FILES:
        result = process_image_sync(image_file)
        results.append(result)

    elapsed_seconds = time.perf_counter() - start_time
    print(f"共處理 {len(IMAGE_FILES)} 張圖片，耗時 {elapsed_seconds:.2f} 秒")
    print("處理結果：", results)


if __name__ == "__main__":
    main()
