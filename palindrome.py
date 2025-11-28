import sys
if len(sys.argv) != 2:
    print("Usage: python palindrome.py <string>")
    sys.exit(1)
string = sys.argv[1]
reverse_str = string[::-1]
if string == reverse_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")