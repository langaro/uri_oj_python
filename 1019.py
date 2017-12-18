import math

s = int(input())

hr = math.floor(s/60/60)
left = s-(hr*60*60)
min = math.floor(left/60)
seg = left-min*60

print('{:d}:{:d}:{:d}'.format(hr, min, seg))