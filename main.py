from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import time

# Hàm nộp bài
def submit_assignment(driver, content, file_path):
    try:
        print(f"[*] Đang nộp bài: {content}...")

        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(file_path)
        time.sleep(2)

        submit_button = driver.find_element(By.CLASS_NAME, "submit__pad__btn") 
        submit_button.click()
        print(f"[+] Đã nộp bài: {content}")
        time.sleep(2)

    except Exception as e: 
        # print(f"[-] Lỗi khi nộp bài {content}: {e}")
        print("[-] Không tìm thấy bài giải trong folder")


def startBot(username, password, login_url, list_url, folder_path, total_pages):
    # Cấu hình Selenium
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Chạy trình duyệt ẩn
    chrome_options.add_argument("--no-sandbox")
    service = Service("C:/Users/lenovo/Desktop/Test/Auto_Submit_CodePtit-main/Auto_Submit_CodePtit-main/chromedriver.exe") # Đường dẫn đến chromedriver.exe
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.delete_all_cookies()         

    try:
        # Đăng nhập
        print("[*] Đang đăng nhập...")
        driver.get(login_url)
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(3)

        # Kiểm tra đăng nhập thành công
        if "login" in driver.current_url:
            print("[-] Đăng nhập thất bại. Kiểm tra lại username và password.")
            return
        print("[+] Đăng nhập thành công!")

        # Duyệt danh sách bài tập
        print("[*] Đang thu thập danh sách bài tập...")
        for page in range(1, total_pages + 1):
            url = f"{list_url}"
            driver.get(url)
            time.sleep(2)

            # Lấy mã HTML của toàn bộ trang
            soup = BeautifulSoup(driver.page_source, "html.parser")
            rows = soup.select("table tbody tr")           
            print(f"\nTrang {page}:")
            for row in rows:
                columns = row.find_all("td")
                if(len(columns) >=4 ):
                    content = columns[2].get_text().strip()  # Lấy mã bài tập
                    title = columns[3].get_text().strip()
                    class_name = row.get("class", [])

                    # Kiểm tra trạng thái bài
                    if "bg--10th" in class_name:
                        print(f"Đã làm: {content}")
                    else:
                        print(f"Chưa làm: {content}")

                        # Truy cập bài tập và nộp bài
                        driver.get(f"{base_url}/{content}")
                        time.sleep(2)
                        file_path = f"{folder_path}/{content} - {title}.cpp" #Thay đổi nếu là ngôn ngữ khác
                        submit_assignment(driver, content, file_path)
                

    except Exception as e:
        print(f"[-] Đã xảy ra lỗi: {e}")
        print("[*] Đã đóng trình duyệt.")
    finally:
        # Đóng trình duyệt
        print("[*] Đã đóng trình duyệt.")
        driver.quit()


# Thông tin đăng nhập và URL
load_dotenv()
username = os.getenv("APP_USERNAME")
password = os.getenv("APP_PASSWORD")
login_url = os.getenv("LOGIN_URL")
list_url = os.getenv("LIST_URL")
base_url=os.getenv("BASE_URL")
folder_path = os.getenv("FOLDER_PATH")
total_pages = int(os.getenv("TOTAL_PAGES"))

# Khởi chạy bot
startBot(username, password, login_url, list_url, folder_path, total_pages)
