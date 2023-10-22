#6번
fw = open("foods.txt", "w")

foods = { "떡볶이": "김밥", "짜장면": "단무지", "라면":"파김치","치킨":"맥주","삼겹살":"소주"}

for i in foods.keys():
    fw.write("%s+%s\n" %(i,foods[i]))

fw.close()
