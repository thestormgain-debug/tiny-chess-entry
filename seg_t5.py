    b[f]=0
    if p=='K' and t-f==2:
        b[26]=b[28]
        b[28]=0
    elif p=='K' and f-t==2:
        b[24]=b[21]
        b[21]=0
    elif p=='k' and t-f==2:
        b[96]=b[98]
        b[98]=0
    elif p=='k' and f-t==2:
        b[94]=b[91]
        b[91]=0
    return (b, 1-dv, nc, ne)
def dl(b, dv, bf, ep, at, a_):
    global NODES, ai, ac
    ai += 1
    dz=bo(b) if dv==0 else -bo(b)
    if dz>=a_:
        return dz
    if dz>at:
        at=dz
    ej=dv==0
    c_=str.isupper if ej else str.islower
    for m in bw(b, dv, bf, ep):
        t=b[m[1]]
        if t==0 or t==-1:
            continue
        bv=am[t.upper()]
        if dz+bv+200<at:
            continue
        nb, ns, nc, ne=cn(b, dv, bf, ep, m)
        if av(nb, nb.index('K' if ej else 'k'), not ej):
            continue
        sc=-dl(nb, ns, nc, ne, -a_, -at)
        if sc>=a_:
            return sc
        if sc>at:
            at=sc
        if ai>ac*2:
            return at
