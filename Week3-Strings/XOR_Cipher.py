"""
Given that we were able to create a Caesar Cipher, let's use a different operation. We'll "XOR" (in Python, ^ ) a given number into each letter to produce a different number, and then we'l use that number to produce a letter instead.

Write a function that takes a string to encrypt and the xor value to encrypt it with.

Step by Step Process
	Loop through each character
		Print each letter

	Convert character to integer => ord(character)
    	Print each character as integer
  
  	Show binary representation => bin(number)
    	Print each binary representation for character
    	Print binary represenation of cipher
    	Show XOR manually and help them understand how to convert number to binary form
  
  	Perform XOR of two integers
    	Manually show XOR
    	Print XOR result
  
  	Convert XOR Result to character => chr(number)
    	Print character of xor result
   		Show ascii table

	Print final result
"""

def xor_cipher(to_encrypt, cipher):
  result = ""
  for i in range(len(to_encrypt)):
    curr_num = ord(to_encrypt[i])
    print("Current number is %s" % curr_num)

    xor_num = cipher ^ curr_num
    result += chr(xor_num)
  print(result)
  return result
 
## Stretch: Write another function that will _decrypt_ the Cipher if you know the xor value to decrypt it with
def xor_decipher(to_decrypt, cipher):
  result = xor_cipher(to_decrypt, cipher)
  return(result)

encrypted = xor_cipher("acab", 4)
xor_decipher(encrypted, 4)