import string

# Password Checker

# Constraints: 
# 1 - The password must have lowercase, uppercase, number and special char
# 2 - The password length must be greater than 9 digits

password = input("Enter the password: ")

def validate_password(password):
    pw_list = list(password)

    requirements = ["lowercase", "uppercase", "numeric", "special character"]

    for char in pw_list:
        if char in string.ascii_lowercase:
            if "lowercase" in requirements:
                requirements.remove("lowercase")
        elif char in string.ascii_uppercase:
            if "uppercase" in  requirements:
                requirements.remove("uppercase")
        elif char in string.digits:
            if "numeric" in requirements:
                requirements.remove("numeric")
        else:
            if "special character" in requirements:
                requirements.remove("special character")

    if len(password) <= 9:
        message = "The password length must be greater than 9"
        return message

    if len(requirements) == 0:
        return "The password is valid!"
    else:
        return f"The following requirements were not met: {requirements}"

check = validate_password(password)

print(check)