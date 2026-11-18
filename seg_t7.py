        if av(nb, nb.index('K' if ej else 'k'), not ej):
            continue
        au=1
        be=b[m[1]] not in (0, -1)
        d=bj-1
        if qi>=3 and bj>=3 and (not be) and (m[0] != b.index('K' if ej else 'k')) and (not av(nb, nb.index('k' if ej else 'K'), ej)):
            d=bj-2
        try:
            sc=-dt(nb, ns, nc, ne, d, -a_, -at, df+1)
        except ValueError:
            print('KING LOST after move', m, 'from board', [(i, b[i]) for i in range(21, 99) if b[i] not in (0, -1)], file=sys.stderr)
            raise
        if sc>at and d<bj-1:
            sc=-dt(nb, ns, nc, ne, bj-1, -a_, -at, df+1)
        if sc>ay:
            ay=sc
            bm=m
        if sc>at:
            at=sc
        if at>=a_:
            if b[m[1]] in (0, -1):
                ag[df]=m
            break
        qi += 1
        if ai>ac:
            break
    if not au:
        return -100000-bj if av(b, b.index('K' if ej else 'k'), not ej) else 0
    fl=0
    if ay<=cx:
        fl=2
    elif ay>=a_:
        fl=1
    TT[kv]=(bj, fl, ay, bm)
    return ay
def az(bq, ci, bc, bz=()):
    global NODES, BUDGET, ai, ac
    ac=bc
    ak.clear()
    TT.clear()
    ag.clear()
