def mutation(s,p,c):
    n_s = list(s)
    n_s[p] = c
    res = "".join(n_s)
    return res

s = input()
p , c = input().split()
result = mutation(s,int(p),c)
print(result)