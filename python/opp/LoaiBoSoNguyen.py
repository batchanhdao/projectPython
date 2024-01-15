file = open('DATA.in','r')
a=[]
while(True):
    s=file.readline().rstrip('\\n')
    # s=input()
    if s=='':break
    li=s.split()
    for j in li:
        try:
            n=int(j)
            if n<-2147483648 or n>2147483647:
                a.append(j)
        except:
            a.append(j)
a.sort()
for j in a:
    print(j,end=' ')

