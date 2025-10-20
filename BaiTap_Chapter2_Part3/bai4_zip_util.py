# Bài 4: Nén và giải nén tệp bằng Python (zip)
# Chạy:
#   - Nén một thư mục: python bai4_zip_util.py zip <thư_mục_nguồn> <đường_dẫn_zip_đích>
#   - Giải nén:         python bai4_zip_util.py unzip <đường_dẫn_zip> <thư_mục_đích>

import sys
import os
import zipfile
from pathlib import Path

def zip_dir(src_dir: str, dst_zip: str) -> None:
    src = Path(src_dir)
    if not src.exists():
        print(f"Thư mục nguồn '{src_dir}' không tồn tại.")
        return
    dst = Path(dst_zip)
    dst.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in src.rglob("*"):
            zf.write(p, p.relative_to(src))
    print(f"Đã nén '{src_dir}' -> '{dst_zip}'")

def unzip_to(src_zip: str, dst_dir: str) -> None:
    sz = Path(src_zip)
    if not sz.exists():
        print(f"File zip '{src_zip}' không tồn tại.")
        return
    dd = Path(dst_dir)
    dd.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(sz, "r") as zf:
        zf.extractall(dd)
    print(f"Đã giải nén '{src_zip}' -> '{dst_dir}'")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in {"zip", "unzip"}:
        print("Cách dùng:")
        print("  python bai4_zip_util.py zip ")
        print("  python bai4_zip_util.py unzip ")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "demo.zip":
        if len(sys.argv) != 4:
            print("Thiếu tham số. Ví dụ: python bai4_zip_util.py zip demo demo.zip")
            sys.exit(1)
        zip_dir(sys.argv[2], sys.argv[3])
    else:
        if len(sys.argv) != 4:
            print("Thiếu tham số. Ví dụ: python bai4_zip_util.py unzip demo.zip out_dir")
            sys.exit(1)
        unzip_to(sys.argv[2], sys.argv[3])