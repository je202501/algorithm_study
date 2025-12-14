T = int(input())
result = 0
for tc in range(T):
    word = input()
    word_check = set()
    for i in range(len(word)):
        if word[i] in word_check:
            if word[i] != word[i-1]:
                break
        else:
            word_check.add(word[i])
        if i == len(word)-1 :
            result +=1

print(result)