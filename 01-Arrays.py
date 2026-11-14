# 1
# array reverse 

a = [1, 2, 3, 4]
left = 0
right = len(a) - 1 

while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1 
    right -= 1

print(a)

# 2
# sorted check 

a = [1, 5, 3, 8]
is_sorted = True
for x in range(0, len(a) - 1, +1):
    if a[x] > a[x + 1]:
        sorted = False
        break

print(sorted)

