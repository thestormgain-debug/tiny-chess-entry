        c=int(7-abs(3.5-f)-abs(3.5-r))
        u=p.upper()
        if p.isupper():
            sc += am[u]+c
            if u=='B':
                wb += 1
            if u=='P':
                sc += (r-1)*4
            if u=='K':
                sc -= 2*c
        else:
            sc -= am[u]+c
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
