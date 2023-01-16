# welcome text
def Welcome():
    print()
    print("Welcome to the Caesar Cipher")
    print()
    print("This program encrypts and decrypts text with the Ceasar Cipher.")
    print()

def enter_message():
    # loop for the encryption and decryption use
    while(True):
        user = input("Would you like to encrypt (e) or decrypt (d): ")
        # asling whether user want to encrypt or decypt 
        if(user == "e"): #if they choose e
            message = input("What message would you like to encrypt: \n")#ask the user what message they want to encrypt
            number = int(input("Enter the shift number: \n"))#and the shift number
            if number>25 or number <0:
                print("Invalid number!! Must not be greater than 25 or smaller than 0")
                continue
            message=message.upper()#changing the message into uppercase
            encrypt(message, number)#calling the encrypt function
            answer = input("Do you want to encrpt or decrypt another message? (y/n)\n")#once the encryption ends ask whether they would want to encrypt another message
            if answer == "y":#if yes call the function above
                enter_message()
            elif answer == "n":#else break the loop
                print("Thank you for using the program, goodbye")
                break
            else:
                print("Invalid Choice!!!")
                continue
        elif(user == "d"):#if they choose d
            message = input("What message would you like to decrypt: ")#ask the user what message they want to decrypt
            number = int(input("Enter the shift number: "))#and the shift number
            message=message.upper()#changing the message into uppercase
            decrypt(message, number)#calling the decrypt function
            answer = input("Do you want to encrpt or decrypt another message? (y/n)")#once the encryption ends ask whether they would want to encrypt another message
            if answer == "y":   #if yes call the function above
                enter_message()
            else:#else break the loop
                print("Thank you for using the program, goodbye")
                break
        else:
            print("Invalid Mode")
            
def encrypt(user_input, shift):
    Encrypted_text = ""#text when converted according to shift number
    for i in user_input:
        if (i.isalpha()!=True):#if i is not not alphabet add it as it is
            Encrypted_text += i
            continue;
        else:
            Encrypted_text += chr((ord(i)+shift-65)%26 + 65)#changing the the letter to ascii code and adding with shift number: which then get subtracted by 65(A) and remainder will be added with 65
    print("Encrypted text: ",Encrypted_text) #printing the encrypted text
    
def decrypt(user_input,shift):#text when converted according to shift number
    Decrypted_text = ""
    for i in user_input:
        if (i.isalpha()!=True):
            Decrypted_text += i#if i is not not alphabet add it as it is
            continue;
        else:
            Decrypted_text += chr((ord(i)-shift-65)%26 + 65)
    print("Decypted text: ",Decrypted_text)
    
def main():
    Welcome()#calling the welcome function
    enter_message() # calling the enter message function
main()