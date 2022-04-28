import sys

MAX = sys.maxsize

large = input()
large = large.split(",")
for i in range(len(large)):
    large[i] = int(large[i])

small = input()
small = small.split(",")
for i in range(len(small)):
    small[i] = int(small[i])

SetSmall = set(small)

Setcurrent = SetSmall.copy()
lptr = 0
rptr = 0
seq_minLen = MAX
seq_minIndex = -1

Dictcurrent = Dictsmall.copy()
while rptr < len(large):
    if large[rptr] in Dictcurrent.keys():
        Dictcurrent[large[rptr]] -= 1
        if Dictcurrent[large[rptr]] == 0:
            Dictcurrent.pop(large[rptr])
    if not Dictcurrent:  # 开始缩lptr
        while large[lptr] not in Dictsmall.keys():
            lptr += 1
        if seq_minLen > rptr - lptr + 1:
            seq_minLen = rptr - lptr + 1
            seq_minIndex = lptr
    rp

print(seq_minIndex + 1)










table = [MAX] * len(large)  # record the length of covering sequence starting at i

for i in range(len(large)):
    Setcurrent = SetSmall.copy()  # record uncovered elements
    for j in range(i, len(large)):
        if large[j] in SetSmall:
            Setcurrent.discard(large[j])
        if not Setcurrent:  # we have find a covering sub sequence
            # determine the length
            table[i] = j - i + 1
            break

seq_minLen = MAX
seq_minIndex = -1

print(table)

for i in range(len(table)):
    if table[i] < seq_minLen:
        seq_minLen = table[i]
        seq_minIndex = i

print(seq_minIndex+1)


'''
1,2,5,4,3,4,7,1,4,9,3,1
3,1,4
'''