s = "31 2"

n = int(s.split(" ")[0]) #n = month
k = int(s.split(" ")[1]) #k = rabbit pair

def rabbits(n,k):
    if n > 40:
        return("n must be <= 40")
    elif k > 5:
        return("k must be <= 5")
    elif n < 2:
        return n
    else:
        return rabbits(n-1,k)+rabbits(n-2,k)*k

# 715827883