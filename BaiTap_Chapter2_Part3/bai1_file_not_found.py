# Bài 1: Xử lý ngoại lệ FileNotFoundError
# Chạy: python bai1_file_not_found.py
# Mục tiêu: minh hoạ cách bắt lỗi khi mở một file không tồn tại.

def safe_read(filename: str) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        msg = f"File '{filename}' không tồn tại."
        print(msg)
        return ""

if __name__ == "__main__":
    # Cố ý mở 1 file không tồn tại để thấy thông báo lỗi
    safe_read("alice.txt")