while True:

    a = input("First: ")
    b = input("Second: ")

    try:
        a = int(a)
        b = int(b)
        break
    except:
        pass

total = 0
for i in range(0,b):
    total += a

print(a,"x",b,"=",total)
