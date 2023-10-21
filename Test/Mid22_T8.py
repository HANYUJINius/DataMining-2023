#8번
scores = [856, 917, 705, 630, 558, 489, 742, 895, 900, 380, 577, 591, 956, 729, 585, 490, 650, 680, 630, 882]
pass_num = 0

for i in scores:
    if (i>=500) and (i<730):
        pass_num += 1
print(pass_num)
