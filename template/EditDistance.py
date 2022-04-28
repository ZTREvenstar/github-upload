def EditDistance(s1, s2):

    # split the string into words
    s1 = s1.split(" ")
    s2 = s2.split(" ")

    # initialize the look-up table matrix
    matrix = [[i + j for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    # perform the look-up calculation
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):

            # if the i-th character of s1 and the j-th character  of s2 are same,
            # they are not needed to edit.
            # the result depends on string s1[:i - 1] and s2[:j - 1]
            if s1[i] == s2[j]:
                matrix[i][j] = matrix[i - 1][j - 1]

            # if different,
            # convert s1[:i] then insert,
            # convert s1[:i-1] then remove,
            # convert s1[:i-1] then substitute
            else:
                matrix[i][j] = min(
                    matrix[i-1][j],
                    matrix[i][j-1],
                    matrix[i-1][j-1]
                ) + 1

    # we only need the last index
    return matrix[len(s1)][len(s2)]


if __name__ == "__main__":

    print("Hello")
    str1 = input()
    str2 = input()

    print(EditDistance(str1, str2))