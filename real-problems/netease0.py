class node:
    def __init__(self, Value):
        self.value = Value
        self.next = None


def exchange(connectHead, head, tail, connectTail):
    if connectHead[0] is not None:
        connectHead[0].next = head[1]
        connectHead[1].next = head[0]
    if connectTail[0] is not None:
        tail[0].next = connectTail[1]
        tail[1].next = connectTail[0]


def mergesort(connectHeadList, headList, tailList, connectTailList, upper, down, keyIndex, A):
    return 0


def merge(connectHeadList, headList, tailList, connectTailList, upper, middle, down, keyIndex, A):
    return 0


if __name__ == "__main__":

    myinput = input()
    myinput = myinput.split()

    N = int(myinput[0])
    M = int(myinput[1])
    Times = int(myinput[2])

    nodeList = []
    # nodeList2 = []

    for i in range(0, N):
        myinput = input()
        myinput = myinput.split(' ')
        print(myinput)

        mynode = node(int(myinput[0]))
        head = mynode

        # mynode2 = node(int(myinput[0]))
        # head2 = mynode2

        for j in range(1, M):

            newnode = node(int(myinput[j]))
            mynode.next = newnode
            mynode = newnode

            # newnode2 = node(int(myinput[j]))
            # mynode2.next = newnode2
            # mynode2 = newnode2

        nodeList.append(head)
        # nodeList2.append(head2)

    # for mynode in nodeList:
    #     print(mynode.value, end='')
    #     print("   ", end='')
    #     while mynode.next is not None:
    #         print(mynode.next.value, end='')
    #         print("   ", end='')
    #         mynode = mynode.next
    #     print("    -----")


    for i in range(0, Times):
        myinput = input()
        myinput = myinput.split()

        r1 = int(myinput[0]) - 1
        r2 = int(myinput[1]) - 1
        c1 = int(myinput[2]) - 1
        c2 = int(myinput[3]) - 1
        s = int(myinput[4])
        A = int(myinput[5])

        connectHeadList = []
        headList = []
        tailList = []
        connectTailList = []

        for j in range(r1, r2 + 1):
            # head
            mynode = nodeList[j]
            for k in range(0, c2 + 1):
                if c1 == 0:
                    connectHeadList.append(None)
                if c2 == M:
                    connectTailList.append(None)
                if k == c1 - 1 and c1 != 0:
                    connectHeadList.append(mynode)
                elif k == c1:
                    headList.append(mynode)
                elif k == c2:
                    tailList.append(mynode)
                    if c2 != M:
                        connectTailList.append(mynode.next)
                mynode = mynode.next

        # begin to sort
        mergesort(connectHeadList, headList, tailList, connectTailList, r1, r2, s, A)

    # finished, output
    for mynode in nodeList:
        print(mynode.value, end='')
        print(" ", end='')
        while mynode.next is not None:
            print(mynode.next.value, end='')
            print(" ", end='')
            mynode = mynode.next


