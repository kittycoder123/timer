import time
def countdown(n):
    if n == 0:
     print("blast off")
    else:
        print (n)
        print('*'*n)
        time.sleep(1)
        countdown(n-1)
a=int(input("enter for how much seconds you want to set a times "))
countdown(a)