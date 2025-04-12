import re

def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r'[A-Z]', password))  # At least one uppercase letter
    lower_criteria = bool(re.search(r'[a-z]', password))  # At least one lowercase letter
    digit_criteria = bool(re.search(r'\d', password))  # At least one number
    special_criteria = bool(re.search(r'[@$!%*?&]', password))  # At least one special character

    # Assess password strength
    if all([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria]):
        strength = "Strong"
        feedback = "Your password is strong! It meets all the security requirements."
    elif any([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria]):
        strength = "Medium"
        feedback = "Your password is medium. Try adding more variety, like uppercase letters, numbers, and special characters."
    else:
        strength = "Weak"
        feedback = "Your password is weak. Please use a combination of uppercase letters, lowercase letters, numbers, and special characters to strengthen it."

    # Return the result
    return strength, feedback


# Test the function
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)
    print(f"Password Strength: {strength}")
    print(feedback)
