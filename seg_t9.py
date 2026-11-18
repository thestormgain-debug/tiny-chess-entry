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

