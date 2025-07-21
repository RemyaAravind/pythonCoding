
#Matching at beginning of string
import re
text = "Hello World"
pattern = r"Hello"

match = re.match(pattern, text)  #
if match:
    print("Match found at beginning")
else:
    print("No match at beginning")



############################################################################

#match entire string
text = "123"
pattern = r"\d+"

if re.fullmatch(pattern, text):
    print("Entire string matches pattern")

#################################################################################
text = "Contact me at john@email.com or jane@example.org"  #.com .in
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

emails = re.findall(pattern, text)
print(emails)  # ['john@email.com', 'jane@example.org']

#####################################################################################

#Replace matches

text = "The date is 2023-12-25"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
replacement = r"\2/\3/\1"  # MM/DD/YYYY format

new_text = re.sub(pattern, replacement, text)
print(new_text)  # The date is 12/25/2023



#########################################################################################

#Split string by pattern
text = "apple,banana;orange:grape"
pattern = r"[,;:]"

parts = re.split(pattern, text)
print(parts)  # ['apple', 'banana', 'orange', 'grape']


########################################################

# Digits
pattern = r"\d+"  # One or more digits
text = "I have 25 apples"
print(re.findall(pattern, text))  # ['25']

# Word characters (letters, digits, underscore)
pattern = r"\w+"  # One or more word characters
text = "hello_world 123"
print(re.findall(pattern, text))  # ['hello_world', '123']

# Whitespace
pattern = r"\s+"  # One or more whitespace characters
text = "hello   world"
print(re.split(pattern, text))  # ['hello', 'world']



##############################################################################################
#Email validation
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

print(validate_email("test@example.com"))  # True
print(validate_email("invalid.email"))     # False

############################################################################################
def extract_phone_numbers(text):  #\b word boundary anchor
    patterns = [
        r"\b\d{3}-\d{3}-\d{4}\b",           # 123-456-7890
        r"\b\(\d{3}\)\s*\d{3}-\d{4}\b",    # (123) 456-7890
        r"\b\d{3}\.\d{3}\.\d{4}\b",        # 123.456.7890
    ]
    
    phone_numbers = []
    for pattern in patterns:
        phone_numbers.extend(re.findall(pattern, text))
    
    return phone_numbers

text = "Call me at 123-456-7890 or (555) 123-4567"
print(extract_phone_numbers(text))

################################################################################################


