# 07
# equillibrium index

a = [5, 6, 2, 3]
prefix = [a[0]]

for idx in range(1, len(a)):
    prefix.append(a[idx-1] + idx)

print(prefix)
