def is_palindrome(s):
    cleaned = ''.join(c for c in s if c.isalnum()).lower()
    def check(sub):
        if len(sub) <= 1:
            return True
        if sub[0] != sub[-1]:
            return False
        return check(sub[1:-1])
    return check(cleaned)

text = input('line of text: ')
if is_palindrome(text):
    print('It is a palindrome!')
else:
    print('It is not a palindrome.')
    
