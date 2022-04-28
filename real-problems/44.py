def equal(str1, str2):
    if len(str1) % 2 != 0:
        # is odd
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                return 0
        return 1
    else:
        mid = int(len(str1) / 2)
        # print(mid)
        # sub1_1 = equal(str1[:mid], str2[:mid])
        # sub1_2 = equal(str1[mid:], str2[mid:])
        # sub2_1 = equal(str1[mid:], str2[:mid])
        # sub2_2 = equal(str1[:mid], str2[mid:])

        if equal(str1[:mid], str2[:mid]) and equal(str1[mid:], str2[mid:]):
            return 1
        elif equal(str1[mid:], str2[:mid]) and equal(str1[:mid], str2[mid:]):
            return 1
        else:
            return 0


if __name__ == "__main__":

    numofCase = input()

    for i in range(0, 2 * int(numofCase)):
        input1 = input()
        input2 = input()

        str1 = []
        str2 = []

        for j in range(0, len(input1)):
            str1.append(input1[j])
            str2.append(input2[j])

        if equal(str1, str2):
            print("YES", end='')
        else:
            print("NO", end='')

        if i != 2 * int(numofCase):
            print()

        while i is not None:
            print("aaa")
