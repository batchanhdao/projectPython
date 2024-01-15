def merge_the_tools(string, k):
    s=string
    kq=''
    for l,c in enumerate(s,1):
        if c not in kq:
            kq=''.join((kq,c))
        if l%k==0:
            print(kq)
            kq=''


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

