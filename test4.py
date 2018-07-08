#排序函数sorted练习。
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def byname(t):
    return t[0].lower()
L1=sorted(L,key=byname)
print(L1)
def bysocre(t):
    return t[1]
L2=sorted(L,key=bysocre)
print(L2)