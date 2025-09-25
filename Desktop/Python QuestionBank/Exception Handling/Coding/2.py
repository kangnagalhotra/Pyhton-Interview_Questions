# Write a program to open a file and catch FileNotFoundError.

try:
    file = open("/Users/kanganagalhotra/Desktop/Python QuestionBank/Exception Handling/Conceptual/1.txt","r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error : File not found")
    
    