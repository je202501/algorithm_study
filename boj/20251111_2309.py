nans = []
for _ in range(9):
    nans.append(int(input()))

nans.sort()
hap = 0
for nan in nans:
    hap += nan

check = False
for i in range(8):
    for j in range(i+1,9):
        if hap - nans[i] - nans[j] == 100:
            check = True
            nans.pop(j)
            nans.pop(i)
            break
    if check:
        break

for nan in nans:
    print(nan)