# 09
# count vowels using in operator with lower() normalization

v = "hello world"
count = 0


for i in v[0:]:
    if i.lower() in "aeiou":
        count += 1

print(count)