import os, sys
KN=(-21, -19, -12, -8, 8, 12, 19, 21)
KG=(-11, -10, -9, -1, 1, 9, 10, 11)
BI=(-11, -9, 9, 11)
RO=(-10, -1, 1, 10)
aa=BI+RO
am={'P': 100, 'N': 320, 'B': 330, 'R': 500, 'Q': 900, 'K': 0}
def bl():
    b=[-1]*120
    for i in range(21, 99):
        if 1<=i % 10<=8:
            b[i]=0
    return b
def cs(s):
    return (int(s[1])+1)*10+ord(s[0])-96
def dx(i):
    return 'abcdefgh'[i % 10-1]+str(i // 10-1)
def db(bq):
    b=bl()
    p=bq.split()
    dq=p[0].split('/')
    for r, dp in enumerate(dq):
        f=1
        for c in dp:
            if c.isdigit():
                f += int(c)
            else:
                b[(9-r)*10+f]=c
                f += 1
    bf=p[2] if len(p)>2 else '-'
    ep=cs(p[3]) if len(p)>3 and p[3] != '-' else 0
    return (b, 0 if p[1]=='w' else 1, bf, ep)
def bo(b):
    sc=0
    wb=bb=0
    for i in range(21, 99):
        p=b[i]
        if p==0 or p==-1:
            continue
        r=i // 10-1
        f=i % 10-1
