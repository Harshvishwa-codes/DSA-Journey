# 08
# Add: max sum of k consecutive elements using sliding window
a = [2, 1, 5, 1, 3, 2]
k = 3
max_sum = 0
window_sum = 0 

for i in range(k):
    window_sum = window_sum + a[i]
    max_sum = window_sum

for x in range(0, len(a)-k):
    window_sum = window_sum + a[x+k] - a[x]
    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)



