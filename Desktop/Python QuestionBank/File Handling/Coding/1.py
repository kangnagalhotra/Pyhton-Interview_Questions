# Read a text file and count number of lines and words.

def count_words(filename):
    try:
        with open(filename,"r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
        print("No of words: " , {word_count})
        print("No of lines: " , {line_count})
    
    except FileNotFoundError:
        print("Error : File not found ")
        
        
    
    