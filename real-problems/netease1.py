def move(bound, location, step, direction):
    # bound[0], location[0] = X
    # bound[0], location[1] = Y

    new_location = location

    # upper
    if direction == 'W':
        if location[1] + step > bound[1]:
            new_location[1] = bound[1]
        else:
            new_location[1] = location[1] + step
    # left
    elif direction == 'A':
        if location[0] - step < 1:
            new_location[0] = 1
        else:
            new_location[0] = location[0] - step
    # down
    elif direction == 'S':
        if location[1] - step < 1:
            new_location[1] = 1
        else:
            new_location[1] = location[1] - step
    # right
    elif direction == 'D':
        if location[0] + step > bound[0]:
            new_location[0] = bound[0]
        else:
            new_location[0] = location[0] + step

    return new_location


def is_visible(Range, playerA, otherPlayer):
    return (abs(playerA[0] - otherPlayer[0]) <= Range) \
           and (abs(playerA[1] - otherPlayer[1]) <= Range)


if __name__ == "__main__":

    myinput = input()
    myinput = myinput.split(' ')

    # for i in range(0, len(myinput)):
    #     print(myinput[i])
    #     # if myinput[i] == ' ':
    #     #     myinput.pop(i)

    M = int(myinput[0])
    N = int(myinput[1])
    playerA_location = [int(myinput[2]), int(myinput[3])]
    R = int(myinput[4])

    K = int(input())
    otherP_locationList = []
    for i in range(0, K):
        myinput = input()
        myinput = myinput.split(' ')
        otherP_locationList.append( [ int(myinput[0]), int(myinput[1]) ] )
        # print("!!!!!   ", end='')
        # print(otherP_locationList[i])

    C = int(input())
    operationList = []
    for i in range(0, C):
        myinput = input()
        myinput = myinput.split(' ')
        tempdict = {'player': int(myinput[0]),
                    'time': int(myinput[1]),
                    'step': int(myinput[2]),
                    'direction': myinput[3]
                    }
        operationList.append(tempdict)

    # sort the operation list according to time
    operationList.sort(key=lambda k: (k.get('time', 0)))

    # for i in operationList:
    #     print(i)
    # print("/////////////////")

    D = int(input())
    queryList = []
    myinput = input()
    myinput = myinput.split(' ')
    for i in range(0, D):
        tempdict = {'time': int(myinput[i]),
                    'order': i}
        queryList.append(tempdict)

    # sort the query list according to time
    queryList.sort(key=lambda k: (k.get('time', 0)))

    # for i in queryList:
    #     print(i)
    # print("/////////////////")

    # query result is stored here, initialize
    queryResult = []
    for i in range(0, D):
        queryResult.append(-1)

    visibleStatus = []
    for i in range(0, D):
        visibleStatus.append(0)

    # start calculating
    numofvisible = 0
    operation_ptr = 0
    for query_ptr in range(0, D):
        # print("query ptr = ", end='')
        # print(query_ptr)
        # print("operation ptr = ", end='')
        # print(operation_ptr)
        while operation_ptr < C and operationList[operation_ptr]['time'] <= queryList[query_ptr]['time']:
            # perform a move
            playerID = operationList[operation_ptr]['player'] - 1
            step = operationList[operation_ptr]['step']
            direction = operationList[operation_ptr]['direction']

            # print("playID = ", end='')
            # print(playerID)
            # print("step = ", end='')
            # print(step)
            # print("direction = ", end='')
            # print(direction)

            otherP_locationList[playerID] = move([M, N], otherP_locationList[playerID], step, direction)
            # update num of visible
            if visibleStatus[playerID] == 0:
                if is_visible(R, playerA_location, otherP_locationList[playerID]):
                    visibleStatus[playerID] = 1
                    numofvisible += 1
            elif visibleStatus[playerID] == 1:
                if is_visible(R, playerA_location, otherP_locationList[playerID]) == 0:
                    visibleStatus[playerID] = 0
                    numofvisible -= 1
            operation_ptr += 1
        # time for a write query result
        queryResult[queryList[query_ptr]['order']] = numofvisible

    # print the result
    for i in range(0, D):
        if i == 0:
            print(queryResult[i], end='')
        else:
            print(" ", end='')
            print(queryResult[i], end='')



