import time


n = int(input())
start_time = time.time()
count = 0

# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if (i%10) == 3 or (i/10) == 3:
#                 count += 1
#             elif (j%10) == 3 or (j/10) == 3:
#                 count += 1
#             elif (k%10) == 3 or (k/10) == 3:
#                 count += 1
#             else:
#                 continue

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)

end_time = time.time()
print("time:",end_time - start_time)