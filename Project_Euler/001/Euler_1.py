count = 0
for x in range (0, 1000):
    three_mod = x % 3
    five_mod = x % 5
    if three_mod == 0 or five_mod == 0:
        count +=  x
print(count)