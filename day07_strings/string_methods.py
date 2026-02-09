# Common String Methods

text = "  KaViTha G  "

# Case methods
print(text.lower())
print(text.upper())
print(text.title())
print(text.capitalize())

# Remove spaces
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Searching
sentence = "machine learning is powerful"
print(sentence.find("learning"))
print(sentence.find("AI"))  # returns -1

# Replace
print(sentence.replace("powerful", "awesome"))

# Split and Join
data = "10,20,30,40"
numbers = data.split(",")
print(numbers)

words = ["I", "love", "Python"]
joined_sentence = " ".join(words)
print(joined_sentence)

# Checking methods
sample = "Python123"
print(sample.isalpha())
print(sample.isdigit())
print(sample.isalnum())
