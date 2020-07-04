import re

dots = []
x = []
y = []

str = list(map(int,re.findall("[\d]+",input())))
for i in range(0,6,2):
    dots.append(str[i:i+2])

for [a, b] in dots:
    if a in x:
        x.remove(a)
    else:
        x.append(a)

    if b in y:
        y.remove(b)
    else:
        y.append(b)

print([*x,*y])
