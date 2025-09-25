# Count word frequency in a string.
from collections import Counter
text = "apple banana apple orange banana apple"
words = text.split()
freq= Counter(words)
print(freq)