1. Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
2. Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. e.g. 
    plain_text = "hello"
    shift = 5
    cipher_text = "mjqqt"
    print output: "The encoded text is mjqqt"
3. Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
4. Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
5. Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text. e.g. 
    cipher_text = "mjqqt"
    shift = 5
    plain_text = "hello"
    print output: "The decoded text is hello"
6. Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

extra stuff:
1. Print the logo from art.py when the program starts.
2. What if the user enters a shift that is greater than the number of letters in the alphabet?
3. Try running the program and entering a shift number of 45.
4. Add some code so that the program continues to work even if the user enters a shift number greater than 26. Hint: Think about how you can use the modulus (%).
5. What happens if the user enters a number/symbol/space?
6. Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?  e.g. start_text = "meet me at 3" end_text = "•••• •• •• 3"
7. Can you figure out a way to ask the user if they want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'. If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again? Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
