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

    # ans = 0

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

    table = [-1 for _ in range(0, Hp + 1)]
    table[Hp] = 0

    def answer_of(n):
        if n > Hp:
            return -1

        if table[n] != -1:
            return table[n]

        ans = 100000
        for dd in damage:
            returnvalue = answer_of(n + dd)
            if returnvalue != -1:
                if returnvalue+1 < ans:
                    ans = returnvalue+1
        # print("!!! in answer_of", n, "value is", ans)
        table[n] = ans
        return ans

    answer = 100000
    for i in range(LowerHp, UpperHp + 1):
        temp_answer = answer_of(i)
        if temp_answer < answer:
            answer = temp_answer

    if answer != 100000:
        print(answer)
    else:
        print(0)
