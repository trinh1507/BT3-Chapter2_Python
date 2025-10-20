# Bài 3: Đếm số từ trong nhiều file với hàm count_words
# Chạy: python bai3_count_words_multi.py
# Có thể sửa danh sách 'filenames' tuỳ ý.

from typing import List

def count_words(filename: str) -> int:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        msg = f"File '{filename}' không tồn tại."
        print(msg)
        return -1
    else:
        words = contents.split()
        num_words = len(words)
        print(f"File '{filename}' có {num_words} từ.")
        return num_words

if __name__ == "__main__":
    filenames: List[str] = ["f1.txt", "f2.txt", "f3.txt"]
    for name in filenames:
        count_words(name)