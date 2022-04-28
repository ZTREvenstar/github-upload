myinput = input()
T = int(myinput[0])

def g(x):
    special = [0, 0, 0, 1]
    if x <= 3:
        return special[x]
    elif x % 2 == 0:
        return g(x / 2) + g(x / 2 - 1)
    elif x % 2 == 1:
        return 2 * g((x - 1) / 2)


def f(x):
    special = [0, 0, 1]
    if x <= 2:
        return special[x]
    elif x % 2 == 0:
        return f(x / 2 - 1) + g(x / 2)
    elif x % 2 == 1:
        return f((x - 1) / 2) + g((x - 1) / 2)


def h(x):
    special = [0, 0, 1]
    if x <= 2:
        return special[x]
    elif x % 2 == 0:
        return h(x / 2) + g(x / 2 - 1)
    elif x % 2 == 1:
        return h((x - 1) / 2) + g((x - 1) / 2)

for ii in range(T):
    x1 = 0
    x2 = 0

    myinput = input()
    n = int(myinput[0])

    #for i in range(3 * n):
