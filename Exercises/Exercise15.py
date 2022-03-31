'''
BMI= weight(kg)/height2(m2)

Enter your weight in (kg): 75
Enter your height in (m): 1.70

Your BMI is: 25.95

You are in the “overweight” range.
'''
weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight/(height*height)
print("Your BMI is:","{0:.2f}".format(bmi))

if(bmi>0 and bmi<=18.5):
    print('You are in the "underweight" range.')
elif(bmi>18.5 and bmi<=24.9):
    print('You are in the "normal" range.')
elif(bmi>24.9 and bmi<=29.9):
    print('You are in the "overweight" range.')
else:
    print('You are in the "obese" range.')




