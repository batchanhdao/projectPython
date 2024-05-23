from pytesseract import pytesseract as pt
import cv2
import os

# Đường dẫn đến thư mục cài đặt Tesseract OCR
path_to_pytesseract = r"C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Thiết lập đường dẫn Tesseract OCR
pt.tesseract_cmd = path_to_pytesseract

# Thiết lập thư mục làm việc
working_directory = r"D:\pythonProject\python\app_python\image_to_text"
os.chdir(working_directory)
print(f"Current working directory: {os.getcwd()}")

# Mở file để ghi kết quả
output_file = open('text.txt', '+a', encoding='UTF-8')

def preprocess_image(img):
    # Chuyển đổi ảnh sang không gian màu HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    # Phân tách các kênh màu
    h, s, v = cv2.split(hsv)

    # Tăng cường độ chói bằng cách tăng giá trị kênh V
    v += 50  # Điều chỉnh giá trị này tùy thuộc vào ảnh cụ thể

    # Gộp các kênh màu lại
    enhanced_hsv = cv2.merge((h, s, v))

    # Chuyển đổi trở lại không gian màu RGB
    enhanced_rgb = cv2.cvtColor(enhanced_hsv, cv2.COLOR_HSV2RGB)

    return enhanced_rgb


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

            # Tiền xử lý ảnh để tăng cường độ chói của số
            processed_img = preprocess_image(img_rgb)

            # Chọn ngôn ngữ: 'eng' hoặc 'vie'
            language = input("Select language ('eng' or 'vie'): ").strip().lower()

            if language == 'vie':
                text = pt.image_to_string(image=processed_img, lang='vie', config='--psm 7 --oem 3')
            else:    
                # Sử dụng config='--psm 6' để nhận dạng các ký tự đơn lẻ
                text = pt.image_to_string(image=processed_img, lang='eng', config='--psm 6 --oem 3')

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
# cv2.imshow("img", processed_img)
# cv2.waitKey(0)
