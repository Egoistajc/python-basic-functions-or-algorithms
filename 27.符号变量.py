
def matcher(t, p):
    # param t: the string to check
    # param p: pattern
    n = len(t)
    m = len(p)
    for i in range(0, n-m+1):
        if p == t[i:i+m]: return True

t=('a','b','c','d')
p=('a','b','c','d')
print(matcher(t,p))
