# multiplicand 被乘數 ; multiplier 乘數
for multiplicand in range(1,10):
    for multiplier in range(1,10):
        print("{}x{}={}".format(multiplicand, multiplier, multiplicand * multiplier),
               end='\t' if multiplier != 9 else '\n')