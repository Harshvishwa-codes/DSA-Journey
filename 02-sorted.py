# 2
# sorted check 

a = [1, 5, 3, 8]
is_sorted = True
for x in range(0, len(a) - 1, +1):
    if a[x] > a[x + 1]:
        sorted = False
        break

print(sorted)