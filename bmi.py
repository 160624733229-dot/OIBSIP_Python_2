def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("===== BMI Calculator =====")

    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height(in meters): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    main()
