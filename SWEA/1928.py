T = int(input())
table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

for tc in range(1,T+1):
    encoded = input()

    binary = ''
    for i in encoded:
        if i in table:
            value = table.index(i)
            binary += format(value,'06b')

    decoded = ''
    for i in range(0,len(binary),8):
        byte = binary[i:i+8]
        decoded += chr(int(byte,2))

    print(f"#{tc} {decoded}")
