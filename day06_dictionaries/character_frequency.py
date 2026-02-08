# Mini Project 4: Character Frequency Counter

text = "engineering"
char_count = {}

for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("Character Frequency:")
for ch, count in char_count.items():
    print(ch, "->", count)
