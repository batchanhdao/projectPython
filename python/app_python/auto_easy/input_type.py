    
class InputText():
    def __init__(self) -> None:
        pass

    def get_input(self, messenge) -> str:
        text = input('NHAP "ex" TO END or ' + messenge).strip()
        if text == 'ex':
            exit()
        return text
    
class InputCut():
    def get_input(self) -> dict:
        result = {"bat_dau": None, "ket_thuc": None}
        text = input('Nhap "no" To Pass or Cut "start, end": ').strip()
        if text == 'no':
            return result
        text = text.split(',')
        if len(text) != 2:
            return result
        if not text[0].isdigit() or not text[1].isdigit():
            return result
        result['bat_dau'] = int(text[0])
        result['ket_thuc'] = int(text[1])
        return result

class InputAdd():
    def get_input(self) -> int:
        text = input('Add "vi tri": ').strip()
        if not text.isdigit():
            return 1
        return int(text)
    
class InputAutoNumber():
    def get_input(self) -> dict:
        result = {"number_start": 1, "len_number": 4}
        text = input('Nhap "no" To Pass or Auto Number "start, lenght number": ').strip()
        if text == 'no':
            return result
        text = text.split(',')
        if len(text) != 2:
            return result
        if not text[0].isdigit() or not text[1].isdigit():
            return result
        result['number_start'] = int(text[0])
        result['len_number'] = int(text[1])
        return result
