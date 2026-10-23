def  check_minimum_length(password):
  if len(password) < 8:
    return ("password length have to be greater than 8")
  else:
     return("The password  meet the required length sucessfully ")
def  check_uppercase_letters(password):
  for character in password:
    if character.isupper() and character.isalpha():
      return "The password have upper case which meet the requirement"
  return "The password must include atleast one uppercase letter"
def check_lowercase_letters(password):
   for character in password:
     if character.islower() and character.isalpha():
       return "The password have lower case and meet the requirement"
   return "The password must include atleast one lowercase letter"
def check_digits(password):
   for character in password:
     if character.isdigit():
       return "the password have digit and meet the requirement"
   return "The password must have atleast one digit"
def check_special_character(password):
   special_characters = "!@#$%^&*()-_+="
   for character in password:
     if character in special_characters:
       return "The password have special character and meet the requirement"
   return "The password must have atleast one special character"
def analyze_password(password):
    check1 = check_minimum_length(password)
    check2 = check_uppercase_letters(password)
    check3 = check_lowercase_letters(password)
    check4 = check_digits(password)
    check5 = check_special_character(password)

    return {
        "Minimum length": check1,
        "Uppercase": check2,
        "Lowercase": check3,
        "Digit": check4,
        "Special character": check5
    }
a=analyze_password("hell123")
print(a)
