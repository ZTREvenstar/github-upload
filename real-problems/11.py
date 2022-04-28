class Solution:
    def solve(self, S):
        # write code here

        # read the input
        S = S[1:len(S) - 1]
        tempTable = S.split(",")
        table1 = []

        for i in tempTable:
            table1.append(int(i))

        table2 = table1.copy()

        # print(table1)

        # table1 is table min
        # table2 is for traverse

        for i in range(1, len(table1)):
            # print("222")
            # print(table2)

            # perform a rotation
            element = table2.pop(0)
            table2.append(element)

            for j in range(0, len(table1)):
                if table1[j] > table2[j]:
                    # update the min
                    table1 = table2.copy()

                if table1[j] < table2[j]:
                    break

        # print the result
        print('{', end='')
        for i in range(0, len(table1)):
            print(table1[i], end='')
            if i != len(table1) - 1:
                print(',', end='')
        print('}')

        output = '{'
        for i in range(0, len(table1)):
            output = output + str(table1[i])
            if i != len(table1) - 1:
                output = output + ','
        output = output + '}'

        return output


if __name__ == "__main__":

    S = input()

    myobj = Solution()

    print(myobj.solve(S))

