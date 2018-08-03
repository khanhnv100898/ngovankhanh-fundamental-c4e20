numbers = [1,6,8,1,2,1,5,6]

n = int(input("Enter number ? "))

count = 0
for i in numbers:
    if i == n:
        count +=1

print("{} appears {} times in my list".format(n,count) )

##
count = numbers.count(n)
print("{} appears {} times in my list".format(n,count) )
