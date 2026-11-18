# 4
# Array/remove duplicates 

a = [0, 0, 0, 1, 1, 3, 3, 5]
x = 1

for i in a[1:]:
    if i != a[x - 1]:
        a[x] = i
        x += 1 

print(a[0:x])
