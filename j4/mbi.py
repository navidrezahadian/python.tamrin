w = float(input('enter weight (kg):'))
h = float(input('enter height (cm):'))
c = ((w) / (h * h * 0.01 * 0.01))


if c < 18.5:
    print('mbi =',c,', thin')
elif c >= 18.5 <= 24.9:
    print('mbi =',c,', normal')
elif c >= 25 <= 29.9:
    print('mbi =',c,', before obesity')
elif c >= 30 <= 34.9:
    print('mbi =',c,', fat')
elif c >= 35:
    print('mbi =',c,', you got fat')