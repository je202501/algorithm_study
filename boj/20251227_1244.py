sw_num = int(input())
list_0 = [0]
sw_input = list(map(int,input().split()))
sw_stat = list_0 + sw_input
st_num = int(input())

for i in range(st_num):
    st = list(map(int,input().split()))
    st_s = st[0]
    st_n = st[1]

    if st_s == 1:
        change = sw_num // st_n
        for j in range(1,change+1):
            ch_n = st_n*j
            sw_stat[ch_n] = 1 - sw_stat[ch_n]
    else:
        sym = True
        sym_ch = 1
        sw_stat[st_n] = 1 - sw_stat[st_n]
        while (sym):
            if st_n - sym_ch < 1 or st_n + sym_ch > sw_num:
                break
            elif sw_stat[st_n - sym_ch] == sw_stat[st_n + sym_ch]:
                sw_stat[st_n - sym_ch] = 1 - sw_stat[st_n - sym_ch]
                sw_stat[st_n + sym_ch] = 1 - sw_stat[st_n + sym_ch]
                sym_ch += 1
            else:
                sym = False

count = 0
for i in range(1,sw_num+1):
    if count == 20:
        print()
        count = 0
    print(sw_stat[i],end = ' ')
    count += 1