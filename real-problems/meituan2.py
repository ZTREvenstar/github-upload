if __name__ == "__main__":
    myinput = input()
    myinput = myinput.split(' ')
    N = int(myinput[0])
    M = int(myinput[1])
    H = int(myinput[2])

    heightList = []
    myinput = input()
    myinput = myinput = myinput.split(' ')
    for item in myinput:
        heightList.append(int(item))

    array = []
    for i in range(0, N):
        array.append(-1)

    if heightList[0] > H:
        array[0] = 0
    else:
        array[0] = 1

    max_len = array[1]
    max_index = 0

    for i in range(1, N):
        if heightList[i] > H:
            array[i] = 0
        else:
            array[i] = array[i-1] + 1
        if array[i] > max_len:
            max_len = array[i]
            max_index = i
    print(array)
    if max_len >= M:
        # 编号等于index + 1
        while heightList[max_index] <= H:
            max_index -= 1
        max_index += 2
        print(max_index)
    else:
        print(-1)
