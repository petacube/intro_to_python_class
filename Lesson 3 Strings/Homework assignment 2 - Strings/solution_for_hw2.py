# Score of string
def alphabetical_score(s):
  score = 0
  for char in s:
    if char.isalpha():  # Check if the character is a letter
      score += ord(char.lower()) - ord('a') + 1
  return score
# Test examples
print(alphabetical_score("Hello"))
print(alphabetical_score("abc"))
print(alphabetical_score("Zebra!"))
