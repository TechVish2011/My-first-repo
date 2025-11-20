# ================================================================
#                 NUMBER ANALYZER – EXPERT EDITION
#       A beautifully improved, feature-rich numeric toolkit
# ================================================================

import random
import math
import time

# ---------------------------------------------------------------
#                     COLOR CODES (for Beauty)
# ---------------------------------------------------------------
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"


# ---------------------------------------------------------------
#               UTILITY & INPUT VALIDATION FUNCTIONS
# ---------------------------------------------------------------

def is_integer_number(num):
    """Return True if num is an integer."""
    return num == int(num)


def get_integer_input(prompt):
    """Safely get an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter an integer.{RESET}")


def get_number_input(prompt):
    """Safely get a float/int."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{RED}❌ Invalid number. Try again.{RESET}")


# ---------------------------------------------------------------
#                      NUMBER PROPERTY CHECKERS
# ---------------------------------------------------------------

def is_prime(num):
    """Efficient Prime Check using 6k ± 1 optimization."""
    if not is_integer_number(num) or num < 2:
        return False
    num = int(num)

    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    k = 5
    while k * k <= num:
        if num % k == 0 or num % (k + 2) == 0:
            return False
        k += 6
    return True


def is_armstrong(num):
    if not is_integer_number(num) or num < 0:
        return False
    digits = str(int(num))
    power = len(digits)
    return sum(int(d) ** power for d in digits) == int(num)


def is_perfect(num):
    if not is_integer_number(num) or num <= 1:
        return False

    num = int(num)
    total = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i
    return total == num


def is_fibonacci(num):
    """Check if a number is in the Fibonacci sequence."""
    if num < 0 or not is_integer_number(num):
        return False
    x = 5 * num * num
    return (int(math.sqrt(x + 4)) ** 2 == x + 4) or (int(math.sqrt(x - 4)) ** 2 == x - 4)


def is_palindrome(num):
    """Check if a number reads the same backwards."""
    s = str(abs(int(num)))
    return s == s[::-1]


def digital_root(num):
    """Return digital root (repeated sum)."""
    num = abs(int(num))
    while num >= 10:
        num = sum(int(d) for d in str(num))
    return num


def reverse_number(num):
    """Return reversed digits."""
    return int(str(abs(int(num)))[::-1])


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def get_factors(num):
    if not is_integer_number(num) or num < 1:
        return []
    num = int(num)
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
    return sorted(factors)


# ---------------------------------------------------------------
#                  ANALYSIS RESULT GENERATION
# ---------------------------------------------------------------

def analyze_basic_properties(num):
    info = {}

    info["Even/Odd"] = "Even" if num % 2 == 0 else "Odd"
    info["Number Type"] = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
    info["Square"] = num ** 2
    info["Cube"] = num ** 3
    info["Square Root"] = math.sqrt(num) if num >= 0 else "Imaginary"

    if is_integer_number(num):
        info["Factors"] = get_factors(abs(num))
        info["Factor Count"] = len(info["Factors"])
        info["Reversed"] = reverse_number(num)
        info["Sum of Digits"] = sum(int(d) for d in str(abs(int(num))))
        info["Digital Root"] = digital_root(num)
    else:
        info["Factors"] = "Only for integers"
        info["Reversed"] = "Only for integers"

    return info


def analyze_special_properties(num):
    props = []
    if is_prime(num):
        props.append("Prime Number")
    if is_armstrong(num):
        props.append("Armstrong Number")
    if is_perfect(num):
        props.append("Perfect Number")
    if is_fibonacci(num):
        props.append("Fibonacci Number")
    if is_palindrome(num):
        props.append("Palindrome Number")

    return props if props else ["No special properties"]


# ---------------------------------------------------------------
#                        MOTIVATIONAL MESSAGES
# ---------------------------------------------------------------

FUN_REPLIES = [
    "🌟 Great work! Keep pushing your limits!",
    "💡 Every number hides a secret. You found it!",
    "🔥 You're improving—keep going!",
    "🚀 Genius mode activated!",
    "✨ Mathematics loves curious minds like you!"
]


def show_message():
    print(f"\n{CYAN}{random.choice(FUN_REPLIES)}{RESET}")


# ---------------------------------------------------------------
#                         MENU OPERATIONS
# ---------------------------------------------------------------

def comprehensive_analysis():
    print(f"\n{BOLD}{BLUE}========== COMPREHENSIVE NUMBER ANALYSIS =========={RESET}")
    num = get_number_input("Enter any number: ")

    print(f"\n{MAGENTA}{BOLD}📌 BASIC PROPERTIES:{RESET}")
    basic = analyze_basic_properties(num)
    for k, v in basic.items():
        print(f"{GREEN}• {k}:{RESET} {v}")

    print(f"\n{YELLOW}{BOLD}⭐ SPECIAL PROPERTIES:{RESET}")
    for prop in analyze_special_properties(num):
        print(f"{GREEN}✓ {prop}{RESET}")

    show_message()


def prime_check():
    num = get_integer_input("\nEnter an integer to check: ")
    print(f"{GREEN}Prime!" if is_prime(num) else f"{RED}Not Prime!{RESET}")
    show_message()


def armstrong_check():
    num = get_integer_input("\nEnter an integer: ")
    if is_armstrong(num):
        print(f"{GREEN}✨ Armstrong Number!{RESET}")
    else:
        print(f"{RED}Not Armstrong.{RESET}")
    show_message()


def perfect_check():
    num = get_integer_input("\nEnter an integer: ")
    if is_perfect(num):
        print(f"{GREEN}⭐ Perfect Number!{RESET}")
    else:
        print(f"{RED}Not Perfect.{RESET}")
    show_message()


def prime_range():
    start = get_integer_input("Start: ")
    end = get_integer_input("End: ")
    if start > end: start, end = end, start

    primes = [n for n in range(start, end + 1) if is_prime(n)]
    print(f"\n{BOLD}Primes:{RESET} {primes}")
    print(f"{GREEN}Total: {len(primes)}{RESET}")
    show_message()


def gcd_lcm_menu():
    print(f"\n{BLUE}{BOLD}GCD & LCM CALCULATOR{RESET}")
    a = get_integer_input("Enter first number: ")
    b = get_integer_input("Enter second number: ")
    print(f"{GREEN}GCD: {gcd(a, b)}{RESET}")
    print(f"{YELLOW}LCM: {lcm(a, b)}{RESET}")
    show_message()


# ---------------------------------------------------------------
#                           MENU SYSTEM
# ---------------------------------------------------------------

def display_menu():
    print(f"""
{CYAN}{BOLD}================= NUMBER ANALYZER – EXPERT EDITION ================={RESET}

  1️⃣  Comprehensive Number Analysis  
  2️⃣  Check Prime Number  
  3️⃣  Check Armstrong Number  
  4️⃣  Check Perfect Number  
  5️⃣  Find All Primes in Range  
  6️⃣  GCD & LCM Calculator  
  7️⃣  Exit  

{CYAN}====================================================================={RESET}
""")


def main():
    while True:
        display_menu()
        choice = input("Enter choice (1–7): ").strip()

        if choice == "1": comprehensive_analysis()
        elif choice == "2": prime_check()
        elif choice == "3": armstrong_check()
        elif choice == "4": perfect_check()
        elif choice == "5": prime_range()
        elif choice == "6": gcd_lcm_menu()
        elif choice == "7":
            print(f"{GREEN}👋 Thanks for using Number Analyzer! Stay curious!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice! Try again.{RESET}")

        input(f"\n{YELLOW}Press Enter to continue...{RESET}")


if __name__ == "__main__":
    main()