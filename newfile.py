# Number Analyzer - A simple and fun tool that gives quick info about any number

import random

def analyze_number(num):
    """Returns a dictionary with info about the number."""
    info = {}

    info["Even/Odd"] = "Even" if num % 2 == 0 else "Odd"
    info["Positive/Negative"] = "Positive" if num >= 0 else "Negative"
    info["Square"] = num ** 2
    info["Cube"] = num ** 3

    # List all factors if integer
    if num == int(num):
        num_int = int(num)
        factors = [i for i in range(1, num_int + 1) if num_int % i == 0]
        info["Factors"] = factors
    else:
        info["Factors"] = "Factors only for integers"

    return info

# Fun psychological / happy replies (20 options)
fun_replies = [
    "🌟 Keep shining, the world needs your light!",
    "😊 Smiles look good on you today!",
    "💪 Every step you take is progress!",
    "🌈 Happiness is contagious—spread it!",
    "🌻 Believe in yourself—you are amazing!",
    "✨ You are stronger than you think!",
    "🥳 Little joys are the big wins!",
    "💖 Keep your heart happy and kind!",
    "🌞 Your positivity brightens the day!",
    "🦋 Change is good—embrace it!",
    "🎉 Celebrate small victories today!",
    "🌙 Rest well—you deserve it!",
    "🔥 Passion fuels greatness!",
    "🌟 You make a difference just by being you!",
    "😊 Happiness is homemade—share it!",
    "💫 Keep your dreams alive!",
    "🌹 Kindness always returns!",
    "🌈 Today is a fresh new start!",
    "💖 Smile, it suits you!",
    "⚡ Believe in magic—you create it!"
]

print("📊 Welcome to Number Analyzer! 🤖")
print("----------------------------------")

try:
    value = float(input("Enter a number: "))
    result = analyze_number(value)

    print("\n🔍 Analysis Result:")
    for key, val in result.items():
        print(f"{key}: {val}")

    # Print a random fun reply
    print("\n💬 Here's a little message for you:")
    print(random.choice(fun_replies))

except ValueError:
    print("❌ Invalid input. Please enter a valid number.")