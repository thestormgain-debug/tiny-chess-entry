            ar=r-1 if ej else 8-r
            v=[0, 10, 20, 35, 60, 100, 180, 0][ar]
            sc += v if ej else -v
    return sc
ai=0
ac=30000
ak=set()
TT={}
ag={}
def dg(b, dv):
    return (tuple(b), dv)
def av(b, sq, ej):
    p='P' if ej else 'p'
    d=-10 if ej else 10
    for dd in (d-1, d+1):
        if b[sq+dd]==p:
            return 1
    n='N' if ej else 'n'
    for dd in KN:
        if b[sq+dd]==n:
            return 1
    k='K' if ej else 'k'
    for dd in KG:
        if b[sq+dd]==k:
            return 1
    for bk, de in ((BI, 'BQ'), (RO, 'RQ')):
        de=de if ej else de.lower()
        for dd in bk:
            t=sq+dd
            while b[t]==0:
                t += dd
            if b[t] != -1 and b[t] in de:
                return 1
    return 0
def bw(b, dv, bf, ep):
    ej=dv==0
    c_=str.isupper if ej else str.islower
    mv=[]
    for sq in range(21, 99):
        p=b[sq]
        if p==0 or p==-1 or (not c_(p)):
