

def compute_closest_to_zero(ts):
    if len(ts) > 0:
        x = ts[0]
        for i in ts:
            for j in ts:
                if abs(i) < abs(j) and abs(i) < abs(x):
                    x = i
        for i in ts:
            if x < 0 and x == -i:
                x = i
    else:
        x = 0
    return x

def factorial(n):
    if n = 0:
        return 1
    else:
        return n * factorial(n-1)

