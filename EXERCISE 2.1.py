#Exercise 2.1
def minarray(xs):
    m = xs[0]
    for x in xs:
        if m > x:
            m = x
    return m

data = [5, 2, 8, 1, 9, 3]
t = minarray(data)
print("Minimum value is:", t)
