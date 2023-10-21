#10번
cnt = 0
number = int(input("몇번까지 게임을 진행하겠습니까?: "))

for i in range(1, number+1):
    for j in str(i):
        if j=='3' or j=='6' or j=='9':
            cnt += 1
print(cnt)
