sheeps = [5,7,300,90,24,50,75]

# 2.1
print("Hello, my name is Khanh and these are my ship sizes :")
print(sheeps)

# 2.2
print("Now my biggest sheep has size", max(sheeps) ,"let's shear it")

# 2.3
maxindex = sheeps.index(max(sheeps))
sheeps[maxindex] = 8

print("After shearing, here is my flock: ")
print(sheeps)

# 2.4
print("One month has passed, now here is my flock")
sheeps= [i +50 for i in sheeps]
print(sheeps)
