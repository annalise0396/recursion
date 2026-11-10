def is_palindrome(s):
  cleaned = ''.join(c for c in s if c.isalnum()).lower()
  return cleaned == cleaned[::-1]


text = input('line of text: ').strip().lower()
if is_palindrome(text):
  print('It is a palindrome!')
else:
  print('It is not a palindrome.')

    
