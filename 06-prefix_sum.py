# 06
# arrays/prefix_sum

a = [2, 4, 6, 5, 3] # [2, 6, 12, 17, 20]
prefix = [a[0]]

for idx in range(1, len(a)):
    prefix.append(a[idx] + prefix[idx - 1])

def range_sum(i, j):
    if i > j or j > (len(a) - 1):
        return ("invalid input")
    elif i == 0:
        return prefix[j]
    else :
        return prefix[j] - prefix[i - 1]

print(range_sum(1, 3))