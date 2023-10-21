#9번
total = 0
useWater = int(input("물의 사용량을 입력해주세요: "))

if(useWater >= 31 ):
    total = 20* 430 + 10*570 + (useWater - 30) * 840
elif(useWater >= 21):
    total = 20* 430 + (useWater - 20) * 570
else: total = useWater * 430

print("총 사용요금은 %d원입니다." %total)
