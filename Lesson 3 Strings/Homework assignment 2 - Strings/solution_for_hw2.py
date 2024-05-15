# Palindrome
import re
def is_palindrome(s):
  # Remove non-alphanumeric characters and convert to lowercase
  normalized_str = re.sub(r'[^A-Za-z0-9]', s).lower()
   # Check if the normalized string is equal to its reverse
  return normalized_str == normalized_str[::-1]

# Test examples
print(is_palindrome("Too bad-I hid a boot"))
print(is_palindrome("A man, a plan, a canal, Panama!"))
print(is_palindrome("Hello, World!"))
 

  
