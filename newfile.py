# Number Analyzer - A simple tool that gives quick info about any number

def analyze_number(num):
    info = {}

    info["Even/Odd"] = "Even" if num % 2 == 0 else "Odd"
    info["Positive/Negative"] = "Positive" if num >= 0 else "Negative"
    info["Square"] = num ** 2
    info["Cube"] = num ** 3

    return info


print("📊 Number Analyzer")
print("---------------------")

try:
    value = float(input("Enter a number: "))
    result = analyze_number(value)

    print("\nAnalysis Result:")
    for key, val in result.items():
        print(f"{key}: {val}")

except ValueError:
    print("❌ Invalid input. Please enter a valid number.")