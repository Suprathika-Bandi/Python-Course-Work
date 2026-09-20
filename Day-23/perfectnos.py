count=0
num=1
with open("perfect_numbers.txt","w") as file:
    while count<3:
        sum=0
        for i in range(1,num):
            if num%i==0:
                sum+=i
        if sum==num:
            file.write(str(num)+"\n")
            count+=1
        num+=1
print("First 3 perfect numbers are written to the file.")
