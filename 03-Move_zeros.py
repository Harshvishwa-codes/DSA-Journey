# 3
# Move zeros

a = [0, 0, 1, 12, 4]
idx = 0

for i in a[0:]:
    if i == 0 :
        continue
    elif i < 0 or i > 0 :
        a[idx] = i 
        idx += 1

for j in range(idx, len(a)):
    a[j] = 0

print(a)