import re

text = "Hello, my phone number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"   # whether any of the string digit is matching
#with the pattern what i have given
match = re.search(pattern, text)

if match:
    
    print(f"Found: {match.group()}")  # Found: 123-456-7890
    print(f"Position: {match.start()}-{match.end()}")  # Position: 26-38