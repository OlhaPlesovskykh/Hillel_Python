password = input("Enter your password: ")
len_string = False
has_digit = False
has_upper = False
has_lower = False
has_alnum = False
score = 0

if len(password) >= 8:
    len_string = True
    score += 1

for char in password:
    if char.isdigit():
        has_digit = True
        score += 1
        break

for char in password:
    if char.isupper():
        has_upper = True
        score += 1
        break

for char in password:
    if char.islower():
        has_lower = True
        score += 1
        break

for char in password:
    if not char.isalnum():
        has_alnum = True
        score += 1
        break

print(f"Password score: {score}")

if not len_string or not has_digit or not has_upper or not has_lower or not has_alnum:
    print("Recommendation:")

if not len_string:
    print("The minimum password length is 8")

if not has_digit:
    print("Use digits")

if not has_upper:
    print("Use capital letters")

if not has_lower:
    print("Use lowercase letters")

if not has_alnum:
    print("Use special characters")
