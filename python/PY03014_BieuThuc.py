for j in range(int(input())):
    v=input()
    st=[]
    dem=1
    kq=''
    for c in v:
        if c=='(':
            kq=kq+str(dem)+' '
            st.append(dem)
            dem+=1
        if c==')':
            kq=kq+str(st.pop())+' '
    print(kq)        