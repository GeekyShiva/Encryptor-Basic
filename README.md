# Encryptor-Basic
This is a simple encryptor/decryptor program developed using python language and can be used to understand the basics of Cryptography 

Cryptography

The science of writing secret codes is called cryptography. For thousands of years cryptography has made secret messages that only the sender and recipient could read, even if someone captured the messenger and read the coded message. A secret code system is called a cipher. The cipher used by the program in this chapter is called the Caesar cipher.

In cryptography, we call the message that we want to be secret the plaintext. The plaintext could look like this:

Hello there! The keys to the house are hidden under the flower pot.

Converting the plaintext into the encoded message is called encrypting the plaintext. The plaintext is encrypted into the ciphertext. The ciphertext looks like random letters, and we cannot understand what the original plaintext was just by looking at the ciphertext. Here is the previous example encrypted into ciphertext:

Yvccf kyviv! Kyv bvpj kf kyv yfljv riv yzuuve leuvi kyv wcfnvi gfk.

But if you know about the cipher used to encrypt the message, you can decrypt the ciphertext back to the plaintext. (Decryption is the opposite of encryption.)

Many ciphers also use keys. Keys are secret values that let you decrypt ciphertext that was encrypted using a specific cipher. Think of the cipher as being like a door lock. You can only unlock it with a particular key.

If you are interested in writing cryptography programs, you can read my other book, “Hacking Secret Ciphers with Python”. It is free to download from http://inventwithpython.com/hacking.

ASCII, and Using Numbers for Letters

How do we implement this shifting of the letters as code? We can do this by representing each letter as a number called an ordinal, and then adding or subtracting from this number to form a new ordinal (and a new letter). ASCII (pronounced “ask-ee” and stands for American Standard Code for Information Interchange) is a code that connects each character to a number between 32 and 126.

The capital letters “A” through “Z” have the ASCII numbers 65 through 90. The lowercase letters “a” through “z” have the ASCII numbers 97 through 122. The numeric digits “0” through “9” have the ASCII numbers 48 through 57. Table 14-1 shows all the ASCII characters and ordinals.

Modern computers use UTF-8 instead of ASCII. But UTF-8 is backwards compatible with ASCII, so the UTF-8 ordinals for ASCII characters are the same as ASCII’s ordinals.
