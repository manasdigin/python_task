height=float(input("your height in m:"))
weight=float(input("your weight in kg:"))
BMI = weight / height**2 
print("your bmi is",BMI)
if BMI <18.5:
    print("BMI Category:underweight")
elif BMI>=18.5 and BMI <=24.9:
    print("BMI category:normal weight")
elif BMI>=25.0 and BMI<=29.9:
    print("BMI catgory :overweight")
else:
    print("BMI category:obese")
 
    