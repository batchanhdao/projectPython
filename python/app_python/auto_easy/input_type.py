from abc import ABC, abstractmethod 

EXIT = 'exit'


class Checking():
    def __init__(self):
        self.exit = False

    def is_exit(self, input_text):
        input_text = input_text.strip().lower()
        if input_text == EXIT:
            self.exit = True
    
class Input():
    def __init__(self) -> None:
        pass
    @abstractmethod
    def get_input(self): 
        pass


class InputText(Input):
    def __init__(self) -> None:
        pass

    def get_input(self, messenge) -> str:
        text = input(messenge).strip()
        check_exit.is_exit(text)
        return text
    
class InputCut(Input):
    def get_input(self) -> dict:
        result = {"bat_dau": None, "ket_thuc": None}
        text = input('Nhap "no" To Pass or Cut "start, end": ').strip()
        if text == 'no':
            return result
        check_exit.is_exit(text)
        try:
            text = text.split(',')
            bat_dau = text[0].strip()
            ket_thuc = text[1].strip()
            if len(text) != 2:
                return result
            if not bat_dau.isdigit() or not ket_thuc.isdigit():
                return result
            if int(bat_dau) < 1 or int(ket_thuc) < 1:
                return result
            if int(bat_dau) > int(ket_thuc):
                return result
            result['bat_dau'] = int(bat_dau)
            result['ket_thuc'] = int(ket_thuc)
            return result
        except Exception as e:
            return result
        
class InputRemove(Input):
    def get_input(self) -> dict:
        result = {"vi_tri": 1, "so_ky_tu": 0}
        text = input('Remove "vị trí, số ký tự muốn xóa": ').strip()
        check_exit.is_exit(text)
        try:
            text = text.split(',')
            if len(text) != 2:
                return result
            vi_tri = text[0].strip()
            so_ky_tu = text[1].strip()
            if not vi_tri.isdigit() or not so_ky_tu.isdigit():
                return result
            if int(vi_tri) < 1 or int(so_ky_tu) < 0:
                return result
            result['vi_tri'] = int(vi_tri)
            result['so_ky_tu'] = int(so_ky_tu)
            return result
        except Exception as e:
            return result

class InputAdd(Input):
    def get_input(self) -> int:
        text = input('Add "vi tri": ').strip()
        check_exit.is_exit(text)
        if not text.isdigit():
            return 1
        if int(text) < 1:
            return 1
        return int(text)
    
class InputAutoNumber(Input):
    def get_input(self) -> dict:
        result = {"number_start": 1, "len_number": 4}
        text = input('Nhap "no" To Pass or Auto Number "start, lenght number": ').strip()
        if text == 'no':
            return result
        check_exit.is_exit(text)
        try:
            text = text.split(',')
            number_start = text[0].strip()
            len_number = text[1].strip()
            if len(text) != 2:
                return result
            if not number_start.isdigit() or not len_number.isdigit():
                return result
            result['number_start'] = int(number_start)
            result['len_number'] = int(len_number)
            return result
        except Exception as e:
            return result


check_exit = Checking()