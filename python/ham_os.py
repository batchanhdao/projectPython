import os
import fnmatch

# Để lấy vị trí của thư mục làm việc hiện tại, os.getcwd() được sử dụng.
print(os.getcwd())
path=os.getcwd()
os.chdir('./python/') 
print(os.getcwd())
path='./python/'

# file = os.path.join(path+'\\class.txt')
# print(file)
# for f in os.listdir(path):
# 	if f.endswith('.txt'):
    # if fnmatch.fnmatch(f, '*.p*'):
# 		print(f)

# # duyệt hết folder
# for (root,dirs,files) in os.walk(path, topdown=True):
# 	print(root)
# 	print(dirs)
# 	print(len(files))
# 	print('--------')
# root: nguồn gốc. dirs: thư mục. files: list file

# change path
# os.chdir('C:\\Users\\Admin\\Downloads')
# print(os.getcwd())
# print(os.listdir())

# of = open(file,'a+',encoding='utf8')
# letter = of.read(10)
# print(letter)
# header = of.readline() 
# print(header, type(header))
# of.write('\nI am Anh')
# of.close()
		
# Phương thức os.makedirs() trong Python được sử dụng để tạo thư mục theo cách đệ quy
# Phương thức os.listdir() trong Python được sử dụng để lấy danh sách tất cả các tệp và thư mục trong thư mục đã chỉ định
print(os.listdir())
# Phương thức os.remove() trong Python được sử dụng để xóa hoặc xóa đường dẫn tệp. 
# os.path.exists()
# folder mom 
print(os.path.dirname(path))
# Trả về thời gian truy cập cuối cùng của đường dẫn .
print(os.path.getatime(path))
# Bình thường hóa trường hợp của tên đường dẫn. 
# os.path.normpath( con đường ) 

# os.path.splitext( con đường ) 
# Chia đường dẫn tên đường dẫn thành một cặp sao cho , và phần mở rộng, ext , trống hoặc bắt đầu bằng một dấu chấm và chứa nhiều nhất một dấu chấm.(root, ext)root + ext == path
# >>> splitext('bar')
# ('bar', '')
# Nếu đường dẫn chứa phần mở rộng thì phần mở rộng sẽ được đặt thành phần mở rộng này, bao gồm cả phần đầu. Lưu ý rằng các khoảng thời gian trước đó sẽ bị bỏ qua:
# >>> splitext('foo.bar.exe')
# ('foo.bar', '.exe')
# >>> splitext('/foo/bar.exe')
# ('/foo/bar', '.exe')