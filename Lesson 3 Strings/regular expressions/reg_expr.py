import re

# Search for a pattern
text = "The quick brown fox jumps over the lazy dog"
pattern = r"fox"
match = re.search(pattern, text)
print(match.group())  # Output: fox

# Find all occurrences of a pattern
matches = re.findall(r"o", text)
print(matches)  # Output: ['o', 'o', 'o', 'o']


text = "apple banana cherry apple orange"
pattern = r"apple"
replacement = "mango"
new_text = re.sub(pattern, replacement, text)
print(new_text)  # Output: mango banana cherry mango orange

text = "apple banana cherry apple orange"
pattern = r"c.*y"
replacement = "mango"
new_text = re.sub(pattern, replacement, text)
print(new_text)  # Output: mango banana cherry mango orange


text = "John Doe: 30 years, Alice: 25 years"
pattern = r"(\w+ \w+): (\d+) years"
matches = re.findall(pattern, text)
for match in matches:
    print(f"Name: {match[0]}, Age: {match[1]}")

#ignoring case
text = "HELLO\nworld"
pattern = r"hello"
match = re.search(pattern, text, re.IGNORECASE)
print(match.group())  # Output: HELLO

#email address validation
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

emails = ["user@example.com", "user.name@example.co.uk", "invalid_email"]
for email in emails:
    print(f"{email}: {is_valid_email(email)}")

