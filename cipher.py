#import art work

from art import logo
print(logo)
# establish lookup alphabet table

alpha = [chr(i) for i in range(97,123)] *2

# define the function
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alpha:
            position = alpha.index(char)        
            new_position = position + shift_amount
            end_text += alpha[new_position]
        else:
            end_text+= char
 
    print(f"The {cipher_direction}d text is : {end_text}")

# check if should run or not
should_end = False
while not should_end:
    direction = input("do you want to encode or decode : (encode/decode)").lower()
    text = input("Enter your message:\n").lower()
    shift= int(input("Type the shift number:\n"))
    shift=shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
# ask if wants to restart

    restart = input("Type 'yes' if you want to do another, or 'no' to exit: \n").lower()
    if restart =='no': 
        should_end= True
        print("Goodbye")