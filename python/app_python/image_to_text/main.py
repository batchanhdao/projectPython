from pytesseract import pytesseract as pt
import cv2
import os

# Đường dẫn đến thư mục cài đặt Tesseract OCR
path_to_pytesseract = r"C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Thiết lập đường dẫn Tesseract OCR
pt.tesseract_cmd = path_to_pytesseract

# Thiết lập thư mục làm việc
working_directory = r"G:\Máy tính khác\My Laptop\pythonProject\python\app_python\image_to_text"
os.chdir(working_directory)
print(f"Current working directory: {os.getcwd()}")

# Mở file để ghi kết quả
output_file = open('text.txt', '+a', encoding='UTF-8')

while True:
    try:
        # Nhập đường dẫn ảnh hoặc 'ex' để kết thúc
        path_to_image = input("ENTER PATH IMAGE or 'ex' to END: ").strip()
        if path_to_image == "ex":
            break
        else:
            # Chuẩn hóa đường dẫn
            path_to_image = os.path.normpath(path_to_image)
            print(f"Selected image: {path_to_image}")

            # Đọc ảnh và chuyển đổi sang định dạng RGB
            img_cv = cv2.imread(path_to_image)
            img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

            # Chọn ngôn ngữ: 'eng' hoặc 'vie'
            language = input("Select language ('eng' or 'vie'): ").strip().lower()

            if language == 'vie':
                text = pt.image_to_string(image=img_rgb, lang='vie')
            else:    
                text = pt.image_to_string(image=img_rgb, lang='eng')

            # Xử lý và ghi kết quả vào file
            lines = [line.strip() for line in str(text).strip().split('\n') if line.strip()]
            print('------------text------------')
            for line in lines:
                print(line)
                output_file.write(line + '\n')

    except Exception as e:
        print(f"Error: {e}")

# Đóng file khi hoàn thành
output_file.close()
# cv2.imshow("img", img_rgb)
# cv2.waitKey(0)
