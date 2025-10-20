

import sys

def count_words_in_file(filename: str) -> int:
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
    # Cho phép truyền tên file từ command line, mặc định dùng 'alice.txt'
    filename = sys.argv[1] if len(sys.argv) > 1 else "alice.txt"
    count_words_in_file(filename)