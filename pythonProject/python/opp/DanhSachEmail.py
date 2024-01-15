file = open('CONTACT.in','r')
di={}
data = file.readlines()
for line in data:
    if line=='': continue
    line=line.strip('\n').strip().lower()
    if line.count('@')==0: continue
    part = line.split('@')
    if len(part[0])==0 or len(part[1])==0: continue
    di[part[0]]=part[1]

di=sorted(di.keys())
for j in di:
    print(j)
file.close()
