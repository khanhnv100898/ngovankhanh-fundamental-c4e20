height_cm = float(input("Chieu cao cua ban la (cm) ? " ))

height_m = height_cm / 100

weight = float(input("Can nang cua ban la (kg) ? "))

BMI = weight / (height_m * height_m)

if BMI < 16 :
    print("Severely underweigh")
elif BMI < 18.5 :
    print("Underweight ")
elif BMI < 25 : 
    print("Normal ")
elif BMI < 30 : 
    print("Overweight ")
else :
    print("Obese ")
