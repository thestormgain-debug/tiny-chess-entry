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
