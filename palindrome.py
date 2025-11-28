import sys
if len(sys.argv) == 2:
    input_string = sys.argv[1]
    print("Usage: python palindrome.py <string>")
else:
    input_string = "hello"     
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
result = is_palindrome(input_string)
if result:
    print("The string is a palindrome. ")
else:
    print("The string is not a palindrome. ")

