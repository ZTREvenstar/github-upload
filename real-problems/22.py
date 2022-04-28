if __name__ == "__main__":

    inputStr = input()

    inputStr = inputStr.split(" ")

    n = int(inputStr[0])

    k = int(inputStr[1])

    #print(n)
    #print("!!!")
    #print(k)

    TimeSlice = []

    for i in range(0, n):
        temp = input()
        TimeSlice.append(int(temp))

    Time = []
    for i in range(0, n):
        Time.append(TimeSlice[i])

    for i in range(0, k):
        output = Time.index(min(Time))
        Time[output] = Time[output] + TimeSlice[output]
        print(output + 1)
