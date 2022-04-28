def myfunction(depth, a):
    if depth <= 5:
        # for i in a:
        #     i += 1
        for i in range(0, len(a)):
            a[i] += 1
        print("!!!!!", end='')
        print(depth, ": ", end='')
        print(a)
        myfunction(depth + 1, a)
    return a


if __name__ == "__main__":

    lists = [0, 1, 2, 3, 4]
    print("before")
    print(lists)

    a = myfunction(0, lists)
    print("after")
    print(lists)