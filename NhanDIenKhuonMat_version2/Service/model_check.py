def User_name(name):
    print(name)
    if len(name) < 3:
        return False
    for j in name.lower():
        if j == ' ':
            continue
        if j >= '0' and j <= '9':
            return False
    return True


def User_msv(msv):
    print(msv)
    msv = msv.lower()
    if len(msv) != 10:
        return False
    if msv[0] != 'b': return False
    for i in msv[1:3]:
        if i < '0' or i > '9':
            return False
    for i in msv[3:7]:
        if i < 'a' or i > 'z':
            return False
    for i in msv[7:]:
        if i < '0' or i > '9':
            return False
    return True
