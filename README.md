## CODE PTIT AUTO SUBMIT

@Author: [MinhTuan](https://github.com/MinLouisCyber)

@Version: 1.0

<img src="https://i.postimg.cc/50s99LSm/Auto-Submit.png" alt="Example" title= "MinhTuan">

### Mục lục

- [Giới thiệu](#giới-thiệu)
- [Tính năng](#tính-năng)
- [Cách cài đặt](#cách-cài-đặt)
- [Cấu hình](#cấu-hình)
- [Cách sử dụng](#cách-sử-dụng)

### Giới thiệu

Bot này giúp người dùng tự động nộp bài tập lập trình trên hệ thống Code PTIT.

- Hỗ trợ đăng nhập và thu thập danh sách bài tập.
- Nộp bài tự động từ thư mục chứa file bài tập đã giải.

### Tính năng

- Tự động đăng nhập vào hệ thống Code PTIT.
- Thu thập danh sách bài tập trên nhiều trang.
- Kiểm tra trạng thái bài tập (đã làm/chưa làm).
- Tự động nộp bài từ file C++ (hoặc các file khác được cấu hình).

### Cách cài đặt

#### Yêu cầu hệ thống

- Python >= 3.8
- Google Chrome và ChromeDriver tương thích

#### Cài đặt

Clone repository:

```bash
git clone https://github.com/MinLouisCyber/Auto_Submit_CodePtit.git
```

Cài đặt các gói Python cần thiết:

```bash
pip install -r requirements.txt
```

Tải và cài đặt ChromeDriver:

- Tải ChromeDriver tại [đây](https://sites.google.com/chromium.org/driver/).
- Đảm bảo ChromeDriver nằm trong PATH hoặc chỉ định đường dẫn trong file `.env`.

### Cấu hình

File `.env`:

```env
APP_USERNAME=your_username_here           # Tên tài khoản PTIT
APP_PASSWORD=your_password_here           # Mật khẩu tài khoản PTIT
LOGIN_URL=https://code.ptit.edu.vn/login
LIST_URL=https://code.ptit.edu.vn/student/question
FOLDER_PATH=/path/to/your/folder          # Đường dẫn đến thư mục chứa bài tập
TOTAL_PAGES=number_of_pages               # Tổng số trang bài tập
```

### Cách sử dụng

#### Tạo file .env

Điền thông tin vào file `.env`:

```env
APP_USERNAME=your_username_here
APP_PASSWORD=your_password_here
LOGIN_URL=https://code.ptit.edu.vn/login
LIST_URL=https://code.ptit.edu.vn/student/question
FOLDER_PATH=/path/to/your/folder
TOTAL_PAGES=number_of_pages
```

Chạy bot:

```bash
python main.py
```

Bot sẽ tự động nộp bài dựa trên cấu hình trong file `.env`.
