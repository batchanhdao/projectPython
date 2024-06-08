    
class InputText():
    def __init__(self) -> None:
        pass

    def get_input(self, messenge) -> str:
        text = input(messenge).strip()
        # if text == 'ex':
        #     exit()
        return text
    
class InputCut():
    def get_input(self) -> dict:
        result = {"bat_dau": None, "ket_thuc": None}
        text = input('Nhap "no" To Pass or Cut "start, end": ').strip()
        if text == 'no':
            return result
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

class InputAdd():
    def get_input(self) -> int:
        text = input('Add "vi tri": ').strip()
        if not text.isdigit():
            return 1
        if int(text) < 1:
            return 1
        return int(text)
    
class InputAutoNumber():
    def get_input(self) -> dict:
        result = {"number_start": 1, "len_number": 4}
        text = input('Nhap "no" To Pass or Auto Number "start, lenght number": ').strip()
        if text == 'no':
            return result
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