words = ["python", "education", "developer"]

no_vowels = [
    "".join(ch for ch in word if ch.lower() not in "aeiou")
    for word in words
]

print(no_vowels)
