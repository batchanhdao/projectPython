def try_except():
    n=input('input number: ')
    try:
        number=int(n)
        print(number+1)
        li=[1,2,3,1]
        a=li.pop()
        print(a,li)
    except Exception:
        print('error input')
    print(123)
def try_else():
    try:
        x = 1/0
        print(x)
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    else:
        print("Nothing wrong.")
def much_except():
    try:
        x = 1/0
        print(x)
    except TypeError:
        print("Data type of variable is not suitable type!")
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    except:
        print("An exception occurred!")
def try_finally():
    try:
        x = 1/0
        print(x)
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    finally:
        print("The 'try except' is finished!")

# try_except()
# try_else()
# much_except()
try_finally()