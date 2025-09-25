# Use finally to close resources.
try:
    
    file = open("/Users/kanganagalhotra/Desktop/Python QuestionBank/Exception Handling/Conceptual/1.txt","r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    try: 
        file.close()
        print("File closed")
    except NameError:
        print("No File to close")
    