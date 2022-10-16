from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
from django.core.exceptions import ValidationError
import re



class MyBcrypt(BCryptSHA256PasswordHasher):
    # Production Value of rounds
    rounds = BCryptSHA256PasswordHasher.rounds + 19

    # Development Value of rounds
    # rounds = BCryptSHA256PasswordHasher.rounds *  2
    ##########

    hasher = BCryptSHA256PasswordHasher()

    def anonymous(self, password):

        salt = self.hasher.salt()
        secret = self.hasher.encode(password, salt)

        return secret


# checker of different signup parameters

class ParameterCheckers:

    def validate_name(name):

        if name.isalpha():
            return name
        else:
            raise ValidationError("Enter a your valid name.")

    def validate_email(email):

        if "@gmail.com" in email:
            return email
        else:
            raise ValidationError("Enter a your valid email address.")

    def validate_username(username):

        if username.startswith("@") and re.match("^[@][A-Za-z]+[0-9]+$", username) and len(username) >= 8:
            return username
        else:
            raise ValidationError("Enter a unique username.")

    def validate_phone(phone):

        if phone.startswith("+") and re.match("^[+][0-9]+$", phone) and len(phone) < 15 and len(phone) >= 12:
            return phone
        else:
            raise ValidationError("Enter a your valid phone number.")

    def validate_password(password):

        x = True

        while x:
            if (len(password) < 6 or len(password) > 75):
                break
            elif not re.search("[a-z]", password):
                break
            elif not re.search("[0-9]", password):
                break
            elif not re.search("[A-Z]", password):
                break
            elif not re.search("[$#@_-`~]", password):
                break
            elif re.search("\s", password):
                break
            else:
                x = False
                break

        if x:
            raise ValidationError("Enter a valid password.")
    
