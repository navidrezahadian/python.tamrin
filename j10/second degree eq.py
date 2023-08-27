import math

print()
print("ax^2 + bx + c=0")

A = float(input("insert A = "))
B = float(input("insert B = "))
C = float(input("insert C = "))

Delta = (B ** 2) - (4 * A * C)

if Delta > 0:
    print("two root".title())
    print(float(-B + math.sqrt(Delta)) / (2 * A))
    print(float(-B - math.sqrt(Delta)) / (2 * A))
elif Delta == 0:
    print(-B / 2 * A)
else :
    print("we don't have any root".title())