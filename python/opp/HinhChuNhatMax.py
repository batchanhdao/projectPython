n=int(input())
a=[int(x) for x in input().split()]
Max=0
for j in range(0,n):
    l,r=j,j
    while(r<=len(a)-2 and a[j]<=a[r+1]): r+=1
    while(l>=1 and a[j]<=a[l-1]): l-=1
    S=a[j]*(abs(j-l)+abs(j-r)+1)
    if S>Max:
        Max=S
print(Max)