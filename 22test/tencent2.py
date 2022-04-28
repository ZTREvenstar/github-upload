def exportAllPrimeLessThan(x):
    array = [i+1 for i in range(0, x)]
    # print(array)
    array[0] = 0  # 1 is not a prime number

    p = 2

    while p < x:
        if array[p - 1] != 0:
            q = p * 2
            while q < x + 1:
                array[q - 1] = 0
                q += p
        p += 1

    answer = []
    for i in array:
        if i != 0:
            answer.append(i)

    return answer


# a = [1, 2, 3, 4]
a = [3, 1, 1, 4, 5, 6]

# !!!!!! ideal index STARTING FROM 1

N = len(a)
# largest prime list
primeList = exportAllPrimeLessThan(N)

# loop, pop, util a have only 1 element
n = len(a)
# ideally index starts from 1
while n != 1:
    temp = []
    # copy a to temp and finally let temp becomes new a
    # only let prime index copy to a
    for prime in primeList:
        if prime > n:
            break
        temp.append(a[prime-1])
    a = temp
    n = len(a)

print("!!!!!!!", a[0])


class Solution:
    def getNumber(self, a):
        # write code here

        return a[0]

