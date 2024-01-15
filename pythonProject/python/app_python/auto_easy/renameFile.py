import os
import fnmatch

def ChangeExtension(path, name, old_extension, new_extension):
	try:
		os.rename(os.path.join(path, name + old_extension) , os.path.join(path, name + new_extension))
		print(name + old_extension + " -> " + name + new_extension)
	except Exception as e:
		print(e)


path = input('ENTER PATH: ')
os.path.normpath(path)
listend=['','txt','java','py','docx','xlsx','csv','jpg','png','webp']
extensions = set()
try:
	for f in os.listdir(path):
		source = os.path.join(path, f)
		name, extension = os.path.splitext(f)
		if os.path.isfile(source):
			extensions.add(extension)
except Exception as e:
	print(e)
print(extensions)

# chon oldend va newend
old_extension=input("ENTER OLD EXTENSION: ")
new_extension=input("ENTER NEW EXTENSION: ")
old_extension = '.' + old_extension
new_extension = '.' + new_extension
try:
	for f in os.listdir(path):
		source = os.path.join(path, f)
		name, extension = os.path.splitext(f)
		if os.path.isfile(source) and f.endswith(old_extension):
			ChangeExtension(path, name, old_extension, new_extension)
		else:
			continue
except Exception as e:
	print(e)

main()