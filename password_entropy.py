import math

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~"

def calculate_entropy(password):
    char_pool = 0

    if any(c in LOWERCASE for c in password):
        char_pool += len(LOWERCASE)
    if any(c in UPPERCASE for c in password):
        char_pool += len(UPPERCASE)
    if any(c in DIGITS for c in password):
        char_pool += len(DIGITS)
    if any(c in SYMBOLS for c in password):
        char_pool += len(SYMBOLS)

    all_known = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS
    for c in password:
        if c not in all_known:
            char_pool += 1

    entropy = len(password) * math.log2(char_pool) if char_pool > 0 else 0
    return entropy

def password_strength(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Reasonable"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"

password = input("Enter your password: ")
entropy = calculate_entropy(password)
strength = password_strength(entropy)

print(f"Password entropy: {entropy:.2f} bits")
print(f"Password strength: {strength}")
