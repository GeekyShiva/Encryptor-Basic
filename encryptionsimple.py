#Hey bruh! heard aboyt cryptography? This program follows simple steps to encrypt/decrypt a string.
#It uses a very simplistic approach for understanding purposes.
#Don't test the brute breaking time of the encryption coz if you do so ? I don't give a F**k :O

result = ''              # variable declaration
message = ''
choice = ''

while choice != '-1':              #loop 1
    choice = input(
        "\nDo you want to encrypt or decrypt the message?\nEnter 1 to Encrypt, 2 to Decrypt, -1 to Exit Program: ")

    if choice == '1':
        message = input("\nEnter the message to encrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)   #The first function ord() converts a character into an integer representing the Unicode of that character
                                                         #The second function chr() does the reverse
        print (result + '\n\n')
        result = ''

    elif choice == '2':
        message = input("\nEnter the message to decrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)

        print (result + '\n\n')
        result = ''

    elif choice != '-1' and choice != '1' and choice != '2':
        print ("You have entered an invalid choice. Please try again.\n\n")


        #bubbye bitch XD XD XD


  #Designed & developed as an experiment/learning purpose by Shivang Shekhar (@geekyshiva)
