test1 = [0,0,0,1,2,3,4,5,6]
i = 0
while i < len(test1):
    if test1[i] == 1 or test1[i] == 2 or  test1[i] == 3:
        test1.pop(0)
    else:
        i+=1
print(test1)
