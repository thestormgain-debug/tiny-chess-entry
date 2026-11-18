    for h in bz:
        ak.add(h)
    b, dv, bf, ep=db(bq)
    ck=set(((cs(m[:2]), cs(m[2:4]), m[4:]) for m in ci))
    co=[m for m in bw(b, dv, bf, ep) if (m[0], m[1], m[2]) in ck]
    if not co:
        return None
    def by(m):
        t=b[m[1]]
        g=am[t.upper()] if t not in (0, -1) else 0
        u=b[m[0]].upper()
        return g
    co.sort(key=lambda m: -by(m))
    ay=co[0]
    for bj in range(1, 9):
        ai=0
        at=-10 ** 9
        bg=None
        for m in co:
            nb, ns, nc, ne=cn(b, dv, bf, ep, m)
            sc=-dt(nb, ns, nc, ne, bj-1, -10 ** 9, -at)
            if sc>at:
                at=sc
                bg=m
            if ai>ac:
                break
        else:
            if bg:
                ay=bg
                co.remove(bg)
                co.insert(0, bg)
            if os.environ.get('DEBUG'):
                print('depth', bj, 'done best', ay if bg else None, file=sys.stderr)
            continue
        if os.environ.get('DEBUG'):
            print('depth', bj, 'partial', file=sys.stderr)
        break
    f, t, pr=ay
    return dx(f)+dx(t)+pr
ad=os.environ.get('MAKEFUN_ENV_URL')
import json, urllib.request, urllib.error
