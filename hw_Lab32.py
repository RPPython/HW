""" A list of strings is given. If each string contains 
the word "strawberries" or "raspberries" 
print the string but append "Yes!" to its end, otherwise append "No!"""

import re

strings = [
  'Ice cream with strawberries?',
  'Ice cream with blueberries?',
  'Ice cream with raspberries?',
  'Ice cream with strawraspberries?',
  'Ice cream with berries?',
]

# Compile the regular expression pattern to match 'strawberries' or 'raspberries'

pattern = re.compile(r'\bstrawberries\b|\braspberries\b', re.IGNORECASE)

# Process each string in the list

for s in strings:
    if pattern.search(s):
        print(f"{s} Yes!")
    else:
        print(f"{s} No!")

# Explanation:

'''
1. The 're' module is imported to use regular expressions.
2. The 'pattern' is compiled to match the words "strawberries" or "raspberries" 
using the word boundaries \b to ensure only the whole words are matched.
3. The 're.IGNORECASE' flag makes the search case-insensitive.
4. The script iterates over each string in the strings list.
If the pattern is found in the string, 
it prints the string with "Yes!" appended; otherwise, 
it prints the string with "No!" appended.'''


