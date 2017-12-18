import math

x1y1 = input().split()
x2y2 = input().split()

x1 = float(x1y1[0])
x2 = float(x2y2[0])
y1 = float(x1y1[1])
y2 = float(x2y2[1])

print("{0:.4f}".format( math.sqrt(((x2-x1)**2)+((y2-y1)**2)) ))