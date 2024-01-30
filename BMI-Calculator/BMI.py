def main():
    try:
        height = float(input("Enter Your Height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))

        bmi = calculate_bmi(height,weight)
        result = interpret_bmi(bmi)
        print(result)
    except ValueError:
        print("Invalid input. Please enter numerical values for height and weight.")


def calculate_bmi(height,weight):
    try:
        bmi = round(weight/(height**2),2)
        return bmi
    except ZeroDivisionError:
        return None


def interpret_bmi(bmi):

    if bmi is None:
        return "Invalid input. Height Should be greater than 0."
    if bmi < 18.5:
        return f"Your BMI is {bmi}, You are underweight."
    elif bmi < 29.9:
        return f"Your BMI is {bmi}, you have a normal Weight."
    elif bmi < 34.9:
        return f"Your BMI is {bmi}, you are obese (Class I)."
    elif bmi < 39.9:
        return f"Your BMI is {bmi}, you are obese (Class II)."
    else:
        return f"Your BMI is {bmi}, you are obese (Class III)."


if __name__=="__main__":
    main()