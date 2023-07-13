"""
Write a program that takes input from user and calculate user's BMI (Body Mass Index).
After calculating the BMI value, print out message indicating the person is 'Underweight', 'Normal', 'Overweight'
or 'Obese'.

Detail about BMI: https://en.wikipedia.org/wiki/Body_mass_index

BMI is calculated using a persons weight and height. BMI is 'weight' divided by square of height.

BMI = weight/(height^2)

The BMI should be classified as follows
Underweight - BMI under or equal to 18.5
Normal - BMI between 18.5 and 25 (not including 18.5 but including 25)
Overweight - BMI between- 25 and 30 (not including 25 but including 30)
Obese - BMI greater than 30

e.g. Input: weight(kg) - 60
            height(m) - 1.9
     Output: Your BMI is 16.6. You are Underweight.

e.g. Input: weight(kg) - 72
            height(m) - 1.84
     Output: Your BMI is 21.3. You are Normal.

e.g. Input: weight(kg) - 72
            height(m) - 1.6
     Output: Your BMI is 27.3. You are Overweight.

e.g. Input: weight(kg) - 70
            height(m) - 1.5
     Output: Your BMI is 31.1. You are Obese.
"""
print("Welcome to BMI calculator!")
weight = input("What is your weight in kg? ")
height = input("What is your height in m? ")


BMI = (int(weight)) / (float(height) * float(height))
BMI_result = round(BMI,1)

if BMI <= 18.5:
    print(f"Your BMI is {BMI_result}. You are Underweight.")
elif (BMI > 18.5) and (BMI <= 25):
    print(f"Your BMI is {BMI_result}. You have a Normal weight.")
elif (BMI > 25) and (BMI <= 30):
    print(f"Your BMI is {BMI_result}. You are Overweight.")
else:
    print(f"Your BMI is {BMI_result}. You are Obese.")
