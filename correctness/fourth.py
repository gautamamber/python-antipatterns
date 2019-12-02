# Bad Exception clause Error

# Always user first the type Error exception clause

# Anti pattern example

try:
    10/0
except Exception as e:
    print(e)
except ZeroDivisionError as z:
    print(z)

# Correct way is

try:
    10/0
except ZeroDivisionError as z:
    print(z)
except Exception as e:
    print(e)

# Move sub class exception clause before its ancestor’s clause