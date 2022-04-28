import sys
from typing import List, Dict


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        def clear(myBoard: str) -> str:
            if myBoard == "":
                return ""
            is_clear = 0
            while not is_clear and myBoard != "":
                l = 0  # left index of a substring
                r = 0  # right index of a substring
                count = 0
                for i in range(len(myBoard)):
                    r = i
                    if myBoard[r] == myBoard[l]:
                        count += 1
                    else:
                        if count >= 3:
                            break
                        l = i
                        count = 1
                    if r == len(myBoard) - 1 and count < 3:
                        is_clear = 1
                if count >= 3:
                    sub1 = myBoard[:l]
                    sub2 = ""
                    if l + count < len(myBoard):
                        sub2 = myBoard[l + count:]
                    myBoard = sub1 + sub2
            return myBoard

        def calcInsertPosition(myBoard: str, myBall: str) -> List:  # discard redundant inserting indexes in myBoard
            myList = []  # here -1 means before myBoard[0], other integers i means after myBoard[i]
            is_diff = 0
            for i in range(len(myBoard)):
                if myBoard[i] != myBall:
                    is_diff = 1
                    break
            if is_diff == 0:
                return [0]
            if myBoard[0] != myBall:  # left end
                myList.append(-1)
            for i in range(len(myBoard) - 1):
                if not (myBoard[i] == myBall and myBoard[i + 1] == myBall):
                    myList.append(i)
            if myBoard[-1] != myBall:  # right end
                myList.append(len(myBoard) - 1)

            return myList

        def refine(myHand: str) -> Dict:
            myDict = {}
            for i in range(len(myHand)):
                if myHand[i] in myDict.keys():
                    myDict[myHand[i]] += 1
                else:
                    myDict[myHand[i]] = 1
            return myDict

        def solve(depth: int, myBoard: str, myHand: Dict, depthControler: List) -> int:
            # print(myBoard, "       ", end='')
            # print(myHand)
            if myBoard == "":
                return 0

            depthControler.append(sys.maxsize)  # store current min depth to solve each subProblem, exactly their answer

            for myBall in myHand.keys():
                if myHand[myBall] == 0:
                    continue
                if depthControler[depth] == 0:
                    break

                currentHand = myHand.copy()
                currentHand[myBall] -= 1
                positions = calcInsertPosition(myBoard, myBall)

                for i in positions:  # traversal all possible positions in current Board
                    if depthControler[depth] == 0:
                        break
                    if i == -1:  # insert at the beginning of string myBoard
                        currentBoard = myBall + myBoard
                    else:  # insert after myBoard[i]
                        currentBoard = myBoard[:i + 1] + myBall + myBoard[i + 1:]

                    depth_allowed = 1  # prevent the recursion from being too deep
                    for counter in range(len(depthControler)):
                        if depth - counter > depthControler[counter]:
                            depth_allowed = 0

                    if depth_allowed:
                        currentBoard = clear(currentBoard)
                        tempNum = solve(depth + 1, currentBoard, currentHand, depthControler)
                        if tempNum < depthControler[depth]:
                            depthControler[depth] = tempNum

            local_result = depthControler.pop(depth)
            if local_result == sys.maxsize:
                return local_result
            else:
                return local_result + 1

        # simplify Hand's structure
        hand = refine(hand)
        solution = solve(0, board, hand, [])
        if solution == sys.maxsize:
            return -1
        else:
            return solution


class Solution2:  # for leetcode. Balls in hand are less than 6
    def findMinStep(self, board: str, hand: str) -> int:

        def clear(myBoard: str) -> str:
            if myBoard == "":
                return ""
            is_clear = 0
            while not is_clear and myBoard != "":
                l = 0  # left index of a substring
                r = 0  # right index of a substring
                count = 0
                for i in range(len(myBoard)):
                    r = i
                    if myBoard[r] == myBoard[l]:
                        count += 1
                    else:
                        if count >= 3:
                            break
                        l = i
                        count = 1
                    if r == len(myBoard) - 1 and count < 3:
                        is_clear = 1
                if count >= 3:
                    sub1 = myBoard[:l]
                    sub2 = ""
                    if l + count < len(myBoard):
                        sub2 = myBoard[l + count:]
                    myBoard = sub1 + sub2
            return myBoard

        def calcInsertPosition(myBoard: str, myBall: str) -> List:  # discard redundant inserting indexes in myBoard
            myList = []  # here -1 means before myBoard[0], other integers i means after myBoard[i]
            is_diff = 0
            for i in range(len(myBoard)):
                if myBoard[i] != myBall:
                    is_diff = 1
                    break
            if is_diff == 0:
                return [0]
            if myBoard[0] != myBall:  # left end
                myList.append(-1)
            for i in range(len(myBoard) - 1):
                if not (myBoard[i] == myBall and myBoard[i + 1] == myBall):
                    myList.append(i)
            if myBoard[-1] != myBall:  # right end
                myList.append(len(myBoard) - 1)

            return myList

        from collections import defaultdict, Counter
        myDict = defaultdict(lambda: 6)
        hand = dict(Counter(hand))  # simplify Hand's structure
        myDict[board] = 0

        def dfs(myBoard: str):
            if myBoard == "":
                return

            for myBall in hand.keys():
                if hand[myBall] <= 0:
                    continue

                hand[myBall] -= 1
                positions = calcInsertPosition(myBoard, myBall)

                for i in positions:  # traversal all possible positions in current Board
                    if i == -1:  # insert at the beginning of string myBoard
                        newBoard = myBall + myBoard
                    else:  # insert after myBoard[i]
                        newBoard = myBoard[:i + 1] + myBall + myBoard[i + 1:]

                    newBoard = clear(newBoard)

                    if myDict[newBoard] > myDict[myBoard] + 1:
                        myDict[newBoard] = myDict[myBoard] + 1
                        dfs(newBoard)

                hand[myBall] += 1

        dfs(board)
        return myDict[""] if myDict[""] < 6 else -1


if __name__ == "__main__":
    myObj = Solution2()
    print(myObj.findMinStep("WRRBBW", "RB"))
    print(myObj.findMinStep("RBYYBBRRB", "YRBGB"))
    print(myObj.findMinStep("G", "GGGGGGG"))
    print(myObj.findMinStep("WWRRBBWW", "WRBRW"))
