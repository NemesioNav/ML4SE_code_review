import random
import string

def generate_random_password(length=12):
    # Combine lowercase letters, uppercase letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has a mix of characters
    password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)

    # Generate the remaining characters of the password
    for _ in range(length - 4):
        password += random.choice(characters)

    # Shuffle the characters to make the password more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Generate a random password with the default length (12 characters)
random_password = generate_random_password()

# Print the generated password
print("Random Password:", random_password)
