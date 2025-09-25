#Write a program to check if a string is a palindrome.

text = input("Enter something: ")
new_text = text[::-1]
if text ==  new_text:
    print("This is palindrome")
else:
    print("This is not palindrome")

    