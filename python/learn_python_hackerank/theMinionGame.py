nguyen_am=['A','E','I','O','U']
def minion_game(string):
    kq={"Kevin":0,"Stuart":0}
    s=string
    for l in range(len(s)):
        if s[l] in nguyen_am:
            kq['Kevin']+=len(s)-l
        else: kq['Stuart']+=len(s)-l
    if kq['Kevin']>kq['Stuart']: 
        print('Kevin '+ str(kq['Kevin']))
    elif kq['Kevin']<kq['Stuart']:
        print('Stuart '+ str(kq['Stuart']))
    else: print('Draw')
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)