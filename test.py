import string

alpha = [chr(i) for i in range(97,123)] *2

direction = input("do you want to encode or decode : (encode/decode)").lower()
text = input("Enter your message:\n").lower()
shift= int(input("Type the shift number:\n"))
if text.isalpha() == False:
    print(f"Text {text} is not alpha")
else:
    print(f"Text {text} is alphabetical")

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alpha.index(letter)        
        new_position = position + shift_amount
        new_letter= alpha[new_position]
        cipher_text += new_letter
    print(f"The encoded text is : {cipher_text}")
 
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alpha.index(letter)
        new_position = position - shift_amount
        new_letter= alpha[new_position]
        plain_text += new_letter
    print(f"The decoded text is : {plain_text}")  


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
