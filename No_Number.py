n = input()

m = list(n)

print(m)
def num():
    if "1" in n :
        q = (m.index("1"))
        m[q] = "one"

    if "2" in n :
        w = (m.index("2"))
        m[w] = "two"

    if "3" in n :
        e = (m.index("3"))
        m[e]= "three"
        
    if "4" in n :
        r = (m.index("4"))
        m[r] = "four"

    if "5" in n :
        t = (m.index("5"))
        m[t] = "five"
        
    if "6" in n :
        y = (m.index("6"))
        m[y] = "six"

    if "7" in n :
        u = (m.index("7"))
        m[u] = "seven"

    if "8" in n :
        o = (m.index("8"))
        m[o] = "eight"

    if "9" in n :
        p = (m.index("9"))
        m[p] = "nine"


num()

if "10" in n :
     s = (n.index("10"))
     m[s] = "ten"
if "0" in n:
    d = (n.index ("0"))    
    m[d] =""
    
print("".join(m))


