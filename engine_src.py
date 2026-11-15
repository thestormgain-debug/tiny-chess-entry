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
        c=int(7-abs(3.5-f)-abs(3.5-r))
        u=p.upper()
        if p.isupper():
            sc += VL[u]+c
            if u=='B':
                wb += 1
            if u=='P':
                sc += (r-1)*4
            if u=='K':
                sc -= 2*c
        else:
            sc -= VL[u]+c
            if u=='b':
                bb += 1
            if u=='p':
                sc -= (8-r)*4
            if u=='k':
                sc += 2*c
    if wb>=2:
        sc += 30
    if bb>=2:
        sc -= 30
    for i in range(21, 99):
        p=b[i]
        if p not in ('P', 'p'):
            continue
        ej=p=='P'
        d_=10 if ej else -10
        dc=1
        for k in (1, 2, 3, 4):
            t=i+d_*k
            if t>98 or t<21:
                break
            for dd in (-1, 0, 1):
                if b[t+dd]==('p' if ej else 'P'):
                    dc=0
                    break
            if not dc:
                break
        if dc:
            r=i // 10-1
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
            continue
        u=p.upper()
        if u=='P':
            bs=10 if ej else -10
            sr=2 if ej else 7
            t=sq+bs
            if b[t]==0:
                if t // 10-1 in (8, 1):
                    for pr in 'qrbn':
                        mv.append((sq, t, pr))
                else:
                    mv.append((sq, t, ''))
                    if sq // 10-1==sr and b[sq+2*bs]==0:
                        mv.append((sq, sq+2*bs, ''))
            for dd in (bs-1, bs+1):
                t=sq+dd
                if t==ep and ep:
                    mv.append((sq, t, ''))
                elif b[t] != -1 and b[t] != 0 and (not c_(b[t])):
                    if t // 10-1 in (8, 1):
                        for pr in 'qrbn':
                            mv.append((sq, t, pr))
                    else:
                        mv.append((sq, t, ''))
        elif u=='N' or u=='K':
            for dd in KN if u=='N' else KG:
                t=sq+dd
                if b[t] != -1 and (b[t]==0 or not c_(b[t])):
                    mv.append((sq, t, ''))
        else:
            bk=BI if u=='B' else RO if u=='R' else aa
            for dd in bk:
                t=sq+dd
                while b[t]==0:
                    mv.append((sq, t, ''))
                    t += dd
                if b[t] != -1 and (not c_(b[t])):
                    mv.append((sq, t, ''))
    if ej:
        if 'K' in bf and b[25]=='K' and (b[26]==0) and (b[27]==0) and (b[28]=='R') and (b[24]==0):
            if not av(b, 25, 0) and (not av(b, 26, 0)) and (not av(b, 27, 0)):
                mv.append((25, 27, ''))
        if 'Q' in bf and b[25]=='K' and (b[24]==0) and (b[23]==0) and (b[22]==0) and (b[21]=='R'):
            if not av(b, 25, 0) and (not av(b, 24, 0)) and (not av(b, 23, 0)):
                mv.append((25, 23, ''))
    else:
        if 'k' in bf and b[95]=='k' and (b[96]==0) and (b[97]==0) and (b[98]=='r') and (b[94]==0):
            if not av(b, 95, 1) and (not av(b, 96, 1)) and (not av(b, 97, 1)):
                mv.append((95, 97, ''))
        if 'q' in bf and b[95]=='k' and (b[94]==0) and (b[93]==0) and (b[92]==0) and (b[91]=='r'):
            if not av(b, 95, 1) and (not av(b, 94, 1)) and (not av(b, 93, 1)):
                mv.append((95, 93, ''))
    return mv
def cn(b, dv, bf, ep, m):
    f, t, pr=m
    b=b[:]
    p=b[f]
    nc=bf
    ne=0
    if p in 'Pp':
        if t==ep and ep:
            b[t-10 if p=='P' else t+10]=0
        if abs(t-f)==20:
            ne=(f+t) // 2
    elif p=='K':
        nc=nc.replace('K', '').replace('Q', '')
    elif p=='k':
        nc=nc.replace('k', '').replace('q', '')
    if f==21 or t==21:
        nc=nc.replace('Q', '')
    if f==28 or t==28:
        nc=nc.replace('K', '')
    if f==91 or t==91:
        nc=nc.replace('q', '')
    if f==98 or t==98:
        nc=nc.replace('k', '')
    if pr and p=='P':
        b[t]=pr.upper()
    elif pr:
        b[t]=pr
    else:
        b[t]=p
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
    global NODES
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
    return at
def dt(b, dv, bf, ep, bj, at, a_, df=0):
    global NODES
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
    global NODES, BUDGET
    ac=bc
    ak.clear()
    TT.clear()
    ag.clear()
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
def dh(dd, bb):
    do=urllib.request.Request(ad+dd, data=json.dumps(bb).encode(), headers={'content-type': 'application/json'})
    with urllib.request.urlopen(do, timeout=120) as r:
        return json.load(r)
def b_(g):
    b, dv, bf, ep=db(g['start_fen'])
    cf=[dg(b, dv)]
    for u in g.get('moves', ()):
        f=cs(u[:2])
        t=cs(u[2:4])
        pr=u[4:]
        b, dv, bf, ep=cn(b, dv, bf, ep, (f, t, pr))
        cf.append(dg(b, dv))
    return cf[:-1]
def cf():
    bc=int(os.environ.get('NODE_BUDGET', '30000'))
    while 1:
        g=dh('/game', {})
        if g.get('status')=='done':
            print('DONE', g.get('wins'), g.get('draws'), g.get('losses'))
            return
        if g.get('status')=='over':
            continue
        mv=az(g['fen'], g['legal_moves'], bc, b_(g))
        if mv is None or mv not in g['legal_moves']:
            mv=g['legal_moves'][0]
        try:
            dh('/move', {'game': g['game'], 'move': mv})
        except Exception:
            g2=dh('/game', {})
            if g2.get('status') in ('your_move',):
                try:
                    dh('/move', {'game': g2['game'], 'move': g2['legal_moves'][0]})
                except Exception:
                    pass
if __name__=='__main__':
    cf()
cf()
