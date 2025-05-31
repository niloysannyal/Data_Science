from collections import Counter

with open("poem.txt","r") as f:
    text = f.read()

words = text.split()
word_counts = Counter(words)
print("maximum occured word: ", word_counts.most_common()[0])