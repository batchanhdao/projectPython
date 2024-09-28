import os
import shutil
from input_type import InputText, InputCut, InputAdd, InputAutoNumber, EXIT, check_exit, InputRemove
from group_type import GroupFileByExtension, GroupFileByFirstLetter, GroupFileByDateDownload
from change_file import FileRename
from logger import FileLogger


class SelectAction():
    def __init__(self) -> None:
        pass

    def select_action(self):
        print("Select action:")
        print("1. Group file by extension")
        print("2. Group file by first letter")
        print("3. Group file by date download")
        print("4. Create new name in files")
        print("5. Cut name in files")
        print("6. Add text in files")
        print("7. Auto number in files")
        print("8. Edit files in folders con")
        print("9. Remove text in name files")
        print("0. Exit")
        action = input("Select action: ").strip()
        return action
    
class Path():
    def __init__(self) -> None:
        pass

    def get_path(self) -> str:
        path = ''
        while True:
            try:
                path = input("Enter path: ").strip()
                check_exit.is_exit(path)
                if check_exit.exit == True: 
                    break
                path = os.path.normpath(path)
                check_path = os.path.exists(path)
                if not check_path:
                    print("Path not found")
                    print("Please enter path again")
                else:
                    break
            except Exception as e:
                print("Error Path Format:", e)
                print("Please enter path again")
        return path

class Main():
    def __init__(self, name_logger):
        self.name_file_logger = 'log ' + str(name_logger) + '.txt'
        self.logger = FileLogger(self.name_file_logger)

    def get_path(self):
        path = Path()
        return path.get_path()

    def get_action(self):
        select_action = SelectAction()
        return select_action.select_action()

from datetime import datetime
if __name__ == '__main__':
    date_time = datetime.now()
    date_time_format = date_time.strftime("%Y-%m-%d %H-%M-%S")
    while True:
        print("Auto Manage Folder")
        print("Input 'exit' to exit")
        print("Present Folder: ", os.getcwd())
        main = Main(date_time_format)
        path = main.get_path()
        logger = main.logger
        if check_exit.exit == True:
            check_exit.exit = False
            print("Exit")
            break

        while True:
            input_text = InputText()
            input_cut = InputCut()
            input_add = InputAdd()
            input_auto_number = InputAutoNumber()
            input_remove = InputRemove()
            action = main.get_action()
            print("action: ", action)
            logger.write(f"Action: {action} - Time: {date_time_format}")
            if action == '1':
                group = GroupFileByExtension(path, logger=logger)
                group.group_files()
            elif action == '2':
                group = GroupFileByFirstLetter(path, logger=logger)
                group.group_files()
            elif action == '3':
                group = GroupFileByDateDownload(path, logger=logger)
                group.group_files()

            elif action == '4':
                file = FileRename(path, logger=logger)
                new_name = input_text.get_input('Enter name new: ')
                number = input_auto_number.get_input()
                vi_tri_add_text = input_add.get_input()
                if check_exit.exit == True:
                    check_exit.exit = False
                    print("Exit")
                    break
                file.create_new_name(new_name=new_name, vi_tri_add_text=vi_tri_add_text, number_start=number['number_start'], len_number=number['len_number'])
            elif action == '5':
                file = FileRename(path, logger=logger)
                vi_tri_cut_name = input_cut.get_input()
                if check_exit.exit == True:
                    check_exit.exit = False
                    print("Exit")
                    break
                file.cut_name_in_file(vi_tri_cut_name=vi_tri_cut_name)
            elif action == '6':
                file = FileRename(path, logger=logger)
                text = input_text.get_input('Enter text: ')
                vi_tri_add_text = input_add.get_input()
                if check_exit.exit == True:
                    check_exit.exit = False
                    print("Exit")
                    break
                file.add_text_to_name(text=text, vi_tri_add_text=vi_tri_add_text)
            elif action == '7':
                file = FileRename(path, logger=logger)
                number = input_auto_number.get_input()
                vi_tri_add_text = input_add.get_input()
                if check_exit.exit == True:
                    check_exit.exit = False
                    print("Exit")
                    break
                file.auto_number(vi_tri_add_text=vi_tri_add_text, number_start=number['number_start'], len_number=number['len_number'])
            elif action == '8':
                file = FileRename(path, logger=logger)
                vi_tri_cut_name = input_cut.get_input()
                number = input_auto_number.get_input()
                vi_tri_add_text = input_add.get_input()
                if check_exit.exit == True:
                    check_exit.exit = False
                    print("Exit")
                    break
                file.edit_files_in_folders_con(vi_tri_cut_name=vi_tri_cut_name, vi_tri_add_text=vi_tri_add_text, number_start=number['number_start'], len_number=number['len_number'])
            
            elif action == '9':
                file = FileRename(path, logger=logger)
                iprm = input_remove.get_input()
                if check_exit.exit == True:
                    check_exit.exit = False
                    print("Exit")
                    break
                file.remove_text_in_name(vi_tri_remove_text=iprm['vi_tri'], len_remove_text=iprm['so_ky_tu'])
                
            elif action == '0':
                print("Exit")
                break
            else:
                print("Action not found")
                print("Please select action again")

