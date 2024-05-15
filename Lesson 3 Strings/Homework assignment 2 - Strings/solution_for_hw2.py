# Shuffle a string
def shuffle_string(s, indices):
   #Creat a list of the same lengh as the string, initialized with empty characters
  shuffled = [''] * len(s)
  for i, index in enumerate(indices):
    shuffled[index] = s[i]
  # Join the list into a single string and return
  return ''.join(shuffled)
# Test examples
print(shuffle_string("abc", [2, 1, 0]))
print(shuffle_string("aiohn", [3, 1, 4, 2, 0]))
print(shuffle_string("art", [1, 0, 2]))
 
