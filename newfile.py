# Number Analyzer - Enhanced Menu-Driven Tool
# A comprehensive number analysis tool with multiple features

import random
import math


# ========================= UTILITY FUNCTIONS =========================

def is_integer_number(num):
    """Check if a number is an integer."""
    return num == int(num)


def get_integer_input(prompt):
    """Get validated integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")


def get_number_input(prompt):
    """Get validated number input from user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


# ========================= NUMBER PROPERTY CHECKS =========================

def is_prime(num):
    """
    Check if a number is prime.
    Optimized algorithm using 6k±1 optimization.
    """
    if not is_integer_number(num) or num < 2:
        return False
    
    num = int(num)
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check divisors up to sqrt(num) using 6k±1 pattern
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    return True


def is_armstrong(num):
    """
    Check if a number is an Armstrong number.
    Armstrong number: sum of its digits raised to the power of number of digits equals the number.
    Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
    """
    if not is_integer_number(num) or num < 0:
        return False
    
    num = int(num)
    num_str = str(num)
    num_digits = len(num_str)
    
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return digit_sum == num


def is_perfect(num):
    """
    Check if a number is a perfect number.
    Perfect number: positive integer equal to the sum of its proper divisors (excluding itself).
    Example: 6 = 1 + 2 + 3
    """
    if not is_integer_number(num) or num <= 1:
        return False
    
    num = int(num)
    divisor_sum = 1  # 1 is always a divisor
    
    # Optimized: check divisors up to sqrt(num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:  # Avoid counting the same divisor twice for perfect squares
                divisor_sum += num // i
    
    return divisor_sum == num


def get_factors(num):
    """Get all factors of an integer efficiently."""
    if not is_integer_number(num) or num < 1:
        return []
    
    num = int(num)
    factors = []
    
    # Optimized: check divisors up to sqrt(num)
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:  # Avoid duplicates for perfect squares
                factors.append(num // i)
    
    return sorted(factors)


# ========================= ANALYSIS FUNCTIONS =========================

def analyze_basic_properties(num):
    """Analyze basic properties of a number."""
    info = {}
    
    info["Even/Odd"] = "Even" if num % 2 == 0 else "Odd"
    info["Positive/Negative/Zero"] = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
    info["Square"] = num ** 2
    info["Cube"] = num ** 3
    info["Square Root"] = math.sqrt(abs(num)) if num >= 0 else f"{math.sqrt(abs(num))}i (imaginary)"
    
    if is_integer_number(num):
        factors = get_factors(abs(num))
        info["Factors"] = factors
        info["Number of Factors"] = len(factors)
    else:
        info["Factors"] = "Only available for integers"
    
    return info


def analyze_special_properties(num):
    """Check special number properties."""
    properties = []
    
    if is_prime(num):
        properties.append("Prime Number")
    
    if is_armstrong(num):
        properties.append("Armstrong Number")
    
    if is_perfect(num):
        properties.append("Perfect Number")
    
    if is_integer_number(num) and num >= 0:
        num_int = int(num)
        
        # Check for perfect square
        sqrt_val = math.isqrt(num_int)
        if sqrt_val * sqrt_val == num_int:
            properties.append("Perfect Square")
        
        # Check for perfect cube (0 and 1 are perfect cubes)
        cube_root = round(num_int ** (1/3))
        if cube_root ** 3 == num_int:
            properties.append("Perfect Cube")
    
    return properties if properties else ["No special properties detected"]


def full_analysis(num):
    """Perform comprehensive analysis on a number."""
    print(f"\n{'='*50}")
    print(f"📊 COMPREHENSIVE ANALYSIS FOR: {num}")
    print(f"{'='*50}\n")
    
    # Basic properties
    print("🔍 Basic Properties:")
    basic_info = analyze_basic_properties(num)
    for key, val in basic_info.items():
        print(f"  {key}: {val}")
    
    # Special properties
    print("\n⭐ Special Properties:")
    special_props = analyze_special_properties(num)
    for prop in special_props:
        print(f"  ✓ {prop}")
    
    print(f"\n{'='*50}\n")


# ========================= MOTIVATIONAL MESSAGES =========================

FUN_REPLIES = [
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


def show_motivational_message():
    """Display a random motivational message."""
    print("\n💬 Here's a little message for you:")
    print(random.choice(FUN_REPLIES))


# ========================= MENU FUNCTIONS =========================

def check_prime_numbers():
    """Menu option: Check if a number is prime."""
    print("\n" + "="*50)
    print("🔢 PRIME NUMBER CHECKER")
    print("="*50)
    num = get_integer_input("Enter an integer to check if it's prime: ")
    
    if is_prime(num):
        print(f"✅ {num} is a PRIME number!")
    else:
        print(f"❌ {num} is NOT a prime number.")
    
    show_motivational_message()


def check_armstrong_numbers():
    """Menu option: Check if a number is Armstrong."""
    print("\n" + "="*50)
    print("💎 ARMSTRONG NUMBER CHECKER")
    print("="*50)
    print("(Armstrong number: sum of digits raised to power of digit count equals the number)")
    num = get_integer_input("Enter a positive integer: ")
    
    if is_armstrong(num):
        num_str = str(num)
        num_digits = len(num_str)
        breakdown = " + ".join([f"{digit}^{num_digits}" for digit in num_str])
        print(f"✅ {num} is an ARMSTRONG number!")
        print(f"   Calculation: {breakdown} = {num}")
    else:
        print(f"❌ {num} is NOT an Armstrong number.")
    
    show_motivational_message()


def check_perfect_numbers():
    """Menu option: Check if a number is perfect."""
    print("\n" + "="*50)
    print("⭐ PERFECT NUMBER CHECKER")
    print("="*50)
    print("(Perfect number: equals the sum of its proper divisors)")
    num = get_integer_input("Enter a positive integer: ")
    
    if is_perfect(num):
        factors = get_factors(num)[:-1]  # Exclude the number itself
        print(f"✅ {num} is a PERFECT number!")
        print(f"   Proper divisors: {factors}")
        print(f"   Sum: {' + '.join(map(str, factors))} = {sum(factors)}")
    else:
        print(f"❌ {num} is NOT a perfect number.")
    
    show_motivational_message()


def comprehensive_analysis_menu():
    """Menu option: Full comprehensive analysis."""
    print("\n" + "="*50)
    print("📊 COMPREHENSIVE NUMBER ANALYSIS")
    print("="*50)
    num = get_number_input("Enter any number: ")
    
    full_analysis(num)
    show_motivational_message()


def batch_prime_finder():
    """Menu option: Find all prime numbers in a range."""
    print("\n" + "="*50)
    print("🔍 BATCH PRIME FINDER")
    print("="*50)
    start = get_integer_input("Enter start of range: ")
    end = get_integer_input("Enter end of range: ")
    
    if start > end:
        start, end = end, start
    
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    
    print(f"\n✅ Prime numbers between {start} and {end}:")
    if primes:
        print(f"   {primes}")
        print(f"   Total count: {len(primes)}")
    else:
        print("   No prime numbers found in this range.")
    
    show_motivational_message()


def display_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("📊 WELCOME TO NUMBER ANALYZER - ENHANCED EDITION 🤖")
    print("="*60)
    print("\n📋 MENU OPTIONS:")
    print("  1. 📊 Comprehensive Number Analysis")
    print("  2. 🔢 Check Prime Number")
    print("  3. 💎 Check Armstrong Number")
    print("  4. ⭐ Check Perfect Number")
    print("  5. 🔍 Find Primes in Range")
    print("  6. 🚪 Exit")
    print("="*60)


def main():
    """Main program loop."""
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            comprehensive_analysis_menu()
        elif choice == "2":
            check_prime_numbers()
        elif choice == "3":
            check_armstrong_numbers()
        elif choice == "4":
            check_perfect_numbers()
        elif choice == "5":
            batch_prime_finder()
        elif choice == "6":
            print("\n👋 Thank you for using Number Analyzer!")
            print("🌟 Keep analyzing and stay curious!")
            break
        else:
            print("\n❌ Invalid choice. Please select 1-6.")
        
        input("\nPress Enter to continue...")


# ========================= PROGRAM ENTRY POINT =========================

if __name__ == "__main__":
    main()
