# Day 6: Dictionaries - Practice

# Q1: Create a dictionary of 5 subjects and marks
# Print subjects with marks > 80

marks = {
    "Maths": 85,
    "Science": 92,
    "English": 78,
    "Social": 88,
    "Tamil": 70
}

print("Q1: Subjects with marks > 80")
for subject, score in marks.items():
    if score > 80:
        print(subject, score)




# Q2: Check if a key exists in dictionary

courses = {
    "Python": 3,
    "Java": 2,
    "C": 1
}

print("Q2: Check if 'Python' exists")
if "Python" in courses:
    print("Python exists")
else:
    print("Python does not exist")



# Q3: Count how many values are greater than 50

numbers = {
    "a": 10,
    "b": 60,
    "c": 80,
    "d": 40,
    "e": 90
}

count = 0
for value in numbers.values():
    if value > 50:
        count += 1

print("Q3: Count of values > 50:", count)


# Q4: Convert two lists into a dictionary


keys = ["name", "age", "city"]
values = ["Kavitha", 20, "Chennai"]

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print("Q4: List to Dictionary")
print(result)



# Q5: First non-repeating character


text = "swiss"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Q5: First non-repeating character")
for ch in text:
    if freq[ch] == 1:
        print(ch)
        break

# Q6: Merge two dictionaries (manual)


d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}

merged = {}

for key, value in d1.items():
    merged[key] = value

for key, value in d2.items():
    merged[key] = value

print("Q6: Merged Dictionary")
print(merged)


# Q7: Invert a dictionary


original = {"a": 1, "b": 2, "c": 3}
inverted = {}

for key, value in original.items():
    inverted[value] = key

print("Q7: Inverted Dictionary")
print(inverted)

# Q8: Word frequency counter

sentence = "python is easy and python is powerful"
words = sentence.split()

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Q8: Word Frequency")
for word, count in word_freq.items():
    print(word, "->", count)


# Q9: Find student with highest marks


scores = {
    "Kavitha": 85,
    "Anu": 90,
    "Ravi": 78
}

topper = ""
max_marks = 0

for name, mark in scores.items():
    if mark > max_marks:
        max_marks = mark
        topper = name

print("Q9: Topper")
print(topper, max_marks)

print("-" * 40)


# Q10: Sort dictionary by values (ascending)

scores = {"A": 85, "B": 90, "C": 78}

items = list(scores.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]

sorted_scores = {}

for key, value in items:
    sorted_scores[key] = value

print("Q10: Dictionary sorted by values")
print(sorted_scores)

