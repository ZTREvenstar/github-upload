"""
1
100 15 20 3
12 16 18

1
20 5 10 3
2 3 4

1
10 8 9 2
3 4
"""

M = int(input())

for test_case_num in range(0, M):

    my_list = map(lambda x: int(x), input().split(" "))
    Hp, LowerHp, UpperHp, N = tuple(my_list)
    damage = []
    my_list = map(lambda x: int(x), input().split(" "))
    for item in my_list:
        damage.append(item)

    #print(Hp, LowerHp, UpperHp, N)
    #print(damage)

    # week state: [LowerHp, Upper Hp]

    ans = 0

    delta2upper = Hp - UpperHp
    delta2lower = Hp - LowerHp

    if damage[0] > delta2lower:
        # all skills damage too high
        print("0")
        continue

    # 1 dao kan si
    skip_flag = 0
    for d in damage:
        if delta2upper <= d <= delta2lower:
            print("1")
            skip_flag = 1
            break
    if skip_flag:
        continue

    # following: if answer exist, it must > 1
    # condition: damage[-1] < Hp - UpperHp

    # the value of table[i] means where i can be reachable from
    # 0 means i is not reachable yet
    table = [0 for _ in range(0, Hp + 1)]
    table[Hp] = Hp

    # here, if we can walk to i from multiple values, table[i] record the largest among them
    for i in range(Hp-1, LowerHp-1, -1):
        for d in damage:
            if i + d <= Hp:
                if table[i+d] != 0:
                    table[i] = i + d

    #print(table)

    # table finished. find answer.
    ans = 100000
    for i in range(UpperHp, LowerHp - 1, -1):
        temp_ans = 0
        x = i
        if table[i] == 0:
            continue
        while table[x] != x:
            x = table[x]
            temp_ans += 1
        if temp_ans < ans:
            ans = temp_ans

    if ans != 100000:
        print(ans)
    else:
        print(0)





