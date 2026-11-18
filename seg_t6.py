    return at
def dt(b, dv, bf, ep, bj, at, a_, df=0):
    global NODES, ai, ac
    ai += 1
    k=dg(b, dv)
    if k in ak:
        return 0
    ed=TT.get((k, bf, ep))
    if ed is not None and ed[0]>=bj:
        fl, sc=(ed[1], ed[2])
        if fl==0:
            return sc
        if fl==1 and sc>=a_:
            return sc
        if fl==2 and sc<=at:
            return sc
    if bj==0:
        return dl(b, dv, bf, ep, at, a_)
    ej=dv==0
    cb=av(b, b.index('K' if ej else 'k'), not ej)
    if bj>=3 and (not cb) and (df>0) and (ai<ac-2000):
        sc=-dt(b, 1-dv, bf, 0, bj-3, -a_, -at, df+1)
        if sc>=a_:
            return sc
    ms=bw(b, dv, bf, ep)
    kv=(k, bf, ep)
    km=ag.get(df)
    ms.sort(key=lambda m: -(am[b[m[1]].upper()] if b[m[1]] not in (0, -1) else 0))
    if ed is not None and ed[3] in ms:
        ms.remove(ed[3])
        ms.insert(0, ed[3])
    if km in ms:
        ms.remove(km)
        ms.insert(1, km)
    au=0
    ay=-10 ** 9
    bm=None
    cx=at
    qi=0
    for m in ms:
        nb, ns, nc, ne=cn(b, dv, bf, ep, m)
