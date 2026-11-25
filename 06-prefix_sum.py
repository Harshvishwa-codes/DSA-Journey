# 06
# arrays/prefix_sum

a = [2, 4, 6, 5, 3]
prefix = [a[0]]

for idx in range(1, len(a)):
    prefix.append(a[idx] + prefix[idx - 1])

print(prefix)