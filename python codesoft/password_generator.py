import string
import random

def generate_password(length):
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the length is appropriate
    if length < 1:
        return "Password length should be at least 1."
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
        except ValueError:
            print("Invalid input! Please enter an integer value.")
            continue
        
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
        another = input("Do you want to generate another password? (yes/no): ")
        if another.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
