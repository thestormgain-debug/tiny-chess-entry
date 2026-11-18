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
