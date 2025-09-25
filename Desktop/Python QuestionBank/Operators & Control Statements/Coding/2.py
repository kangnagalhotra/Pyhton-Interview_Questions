#Count vowels, consonants, digits, and spaces in a string.

text = "Python is a integrated language and version is 3.7"
vowels=["a","e","i","o","u","A","E","I","O","U"]

vowels_count =0 
consonants_count =0
digits_count = 0
spaces_count = 0

for ch in text:
    if ch in vowels:
        vowels_count+=1
    elif ch.isalpha():
        consonants_count+=1
    elif ch.isnumeric():
        digits_count+=1
    elif ch.isspace():
        spaces_count+=1
        
print("Vowels Count: ", vowels_count)
print("Consonants Count: ", consonants_count)
print("Digits Count: ", digits_count)
print("Space Count: ", spaces_count)


    
        