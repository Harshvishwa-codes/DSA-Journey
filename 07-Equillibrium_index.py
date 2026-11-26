# 07
# equillibrium index

a = [1, 3, 5, 2, 2]
prefix = [a[0]]

for idx in range(1, len(a)):
    prefix.append(a[idx] + prefix[idx-1])

def range_sum(i, j):
    if i > j or j > len(a) - 1:
        return 0
    elif i == 0 :
        return prefix[j]
    else :
        return prefix[j] - prefix[i-1]

result = -1 

for k in range(len(a)):
    left = range_sum(0, k - 1)
    right = range_sum(k + 1, len(a) - 1)
    if left == right :
        result = k
        break

print(result)