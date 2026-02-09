# Practice Questions 

# 1. Reverse a string
s = "python"
reverse = ""

for ch in s:
    reverse = ch + reverse

print("Reversed string:", reverse)

# 2. Count vowels
sentence = "education"
vowel_count = 0

for ch in sentence:
    if ch in "aeiouAEIOU":
        vowel_count += 1

print("Vowel count:", vowel_count)

# 3. Palindrome check
word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 4. Character frequency
text = "banana"
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print("Character frequency:", frequency)

# 5. Remove duplicate characters
text = "programming"
result = ""

for ch in text:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)

# 6. Count words in a sentence
s = "I love Python programming"
print("String :",s)
print("No.of words in the sentence :",len(s.split()))


# 7. Find longest word
s = "Python is very powerful language"
words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word
print("String :",s)
print("Longest word is :",longest)


# 8. Replace spaces with underscore
s = "machine learning model"
print("Original String :",s)
print("After Replacing : ",s.replace(" ", "_"))
  
