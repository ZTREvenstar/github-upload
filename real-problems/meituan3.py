myinput = input()
myinput = myinput.split()

M = int(myinput[0])

for i in range(0, M):
    myinput = input()
    myinput = myinput.split()
    x = int(myinput[0])
    a = int(myinput[1])
    b = int(myinput[2])
    n = int(myinput[3])

    profit = 0
    for step in range(0, n):
