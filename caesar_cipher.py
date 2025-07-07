def encrypt(text, shift):
    result = ""
    for character in text:
           if character.isalpha():
               shift_base = ord("A") if character.isupper() else ord("a")
               result += character((ord(character) - shift_base + shift) % 26 + shift_base)
           else:
                   result += character
    return result
