def encrypt(text, shift):
    result = ""
    for character in text:
        if character.isalpha():
            shift_base = ord("A") if character.isupper() else ord("a")
            result += character((ord(character) - shift_base + shift) % 26 + shift_base)
        else:
            result += character
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

#the main program
def main():
    print("Welcome to a Ceaser Cipher Program!")
    choice = input("would you like to encrypt or decrypt? e/d: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (number):"))

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print("Encrypt Message:", encrypted)
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print("Decrypted Message:", decrypted)
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

if __name__=="__main__":
     main()

    