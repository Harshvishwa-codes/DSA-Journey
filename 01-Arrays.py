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
