# Score of string
def string_score(s):
  score = 0
  for i in range(len(s) - 1):
    score += abs(ord(s[i]) - ord(s[i + 1]))
  return score
# Test examples
print(string_score("Hello"))
print(string_score("abc"))
print(string_score("Zebra!"))
