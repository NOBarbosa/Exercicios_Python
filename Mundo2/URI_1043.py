from math import fabs
x = input().split()
r1, r2, r3 = x
r1 = float(r1)
r2 = float(r2)
r3 = float(r3)
if fabs(r2- r3) < r1 and (r2 + r3) > r1:
    if fabs(r1-r3) < r2 and (r1+r3) > r2:
        if fabs(r1-r2)< r3 and (r1+r2) > r3:
            print('Perimetro = {:.1f}'.format(r1 + r2 + r3))
else:
    print('Area = {:.1f}'.format((r1+r2)*(r3/2)))