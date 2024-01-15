
# if __name__ == '__main__':
#     students=[]
#     min1,min2=float(10**9),float(10**9)
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         if min1>score:
#             min2=min1
#             min1=score
#         elif min2>score and min1<score:
#             min2=score
#         students.append([name,score])
#     students = sorted(students,key = lambda x:x[0])
#     for l in range(len(students)):
#         if students[l][1]==min2:
#             print(students[l][0])

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = [float(x) for x in line]
#         student_marks[name] = scores
#     query_name = input()
#     print("{:.2f}".format(sum(student_marks.get(query_name))/3))

def List():
    if __name__ == '__main__':
        li=[]
        N = int(input())
        for l in range(N):
            lenh = [x for x in input().split()]
            if lenh[0] == 'insert':
                li.insert(int(lenh[2]),int(lenh[1]))
            elif lenh[0] == 'append':
                li.append(int(lenh[1]))
            elif lenh[0] == 'print':
                print(li)
            elif lenh[0] == 'remove':
                li.remove(int(lenh[1]))
            elif lenh[0] == 'sort':
                li.sort()
            elif lenh[0] == 'pop':
                li.pop()
            else: li.reverse()

def Hash():
    if __name__=='__main__':
        n=int(input())
        li = tuple(int(x) for x in input().split())
        print(hash(li))
                

