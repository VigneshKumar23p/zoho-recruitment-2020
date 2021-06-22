string = input()
i=0
count=0
a=[]
for i in string:
    count+=1
middle=count//2

rows = count
for i in range(1,rows+1):
    num = count//2
    for j in range(rows,0,-1):
        if(j > i):
            print(" ",end=' ')
        else:
            print(string[num],end=' ')
            if(num >= count-1):
                num = 0
            else:
                num = num+1
    print("")

