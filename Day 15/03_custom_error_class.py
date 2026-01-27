
class ValidationError(Exception):
    """Base class for validation errors"""
    pass


class UsernameError(ValidationError):
    pass


class PasswordError(ValidationError):
    pass


class EmailError(ValidationError):
    pass



def register_user(username, password, email):
    if len(username) < 4:
        raise UsernameError("Username must be at least 4 characters")

    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters")

    if "@" not in email:
        raise EmailError("Invalid email address")

    return {
        "status": "success",
        "message": "User registered successfully"
    }



try:
    response = register_user(
        username="ri",
        password="12345",
        email="rishovgmail.com"
    )
    print(response)

except UsernameError as e:
    print("400 Bad Request:", e)

except PasswordError as e:
    print("400 Bad Request:", e)

except EmailError as e:
    print("400 Bad Request:", e)

except ValidationError as e:
    print("Validation Error:", e)
