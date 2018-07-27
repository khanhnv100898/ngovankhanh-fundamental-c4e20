sheeps = [5,7,300,90,24,50,75]

#2.5
print("Hello, my name is Khanh and these are my ship sizes :")
print(sheeps)
maxindex = sheeps.index(max(sheeps))
sheeps[maxindex] = 8

print("After shearing, here is my flock: ")
print(sheeps)

for k  in range(1,4):
    if k != 3:
        print("Month",k)
        print("One month has passed, now here is my flock")
        sheeps= [i +50 for i in sheeps]
        print(sheeps)

        print("Now my biggest sheep has size", max(sheeps) ,"let's shear it")

        maxindex = sheeps.index(max(sheeps))
        sheeps[maxindex] = 8
        print("After shearing, here is my flock: ")
        print(sheeps)
    else:
        print("Month",k)
        print("One month has passed, now here is my flock")
        sheeps= [i +50 for i in sheeps]
        print(sheeps)
        total = 0
        for size in range(len(sheeps)):
            total += sheeps[size]
            print("My flock has size in total ",total)
            print("I would get",total,"* 2$ = ",total *2,"$")



    




