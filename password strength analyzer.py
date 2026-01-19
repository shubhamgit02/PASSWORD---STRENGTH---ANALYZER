import re
import math

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'\d', password):
        charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}/|<>]', password):
        charset += 32
    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset)
    return entropy
def check_common_patterns(password):
    common_patterns = ['123', 'abc', 'password', 'qwerty', 'letmein', 'admin', 'sss']
    for pattern in common_patterns:
        if pattern in password.lower():
            return True
    return False 
def evaluate_password_strength(password):
    entropy = calculate_entropy(password)
    has_common_patterns = check_common_patterns(password)
    if has_common_patterns or len(password) < 6:
        return 'Weak'
    elif entropy < 40:
        return 'Moderate'
    else:
        return 'Strong'
    
    # Taking User Input
user_password = input("Enter a password to check its strength: ")
print(f"Password Strength: {evaluate_password_strength(user_password)}")