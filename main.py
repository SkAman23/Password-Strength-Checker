import re

def check_password_strength(password):
    score = 0
    feedback = []


    #Check Length
    if len(password) < 8 :
        feedback.append("Password is too short. It should be at least 8 character long.")
    else:
        score += 1

    #Check for uppercase
    if re.search(r"[A-Z]", password): #raw string (special characters like \ )
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    #Check for lowercase
    if re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    #Check for digits
    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("Add numbers.")
    
    #Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]",password):
        score += 1
    else:
        feedback.append("Add special characters.")

    #Determine strength based on score 
    if score < 3:
        strength = "Weak"
    elif score < 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength,feedback


#Test the function
password = input("Enter your Password :")
strength, feedback = check_password_strength(password)

print(f"Password Strength : {strength}")#formatted string literal (Convert it to a string)
if feedback:
    print("Suggestions for improvement :")
    for suggestion in feedback:
        print(f"- {suggestion}")
else:
    print("Great! Your password is strong.")