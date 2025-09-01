from collections import deque
def is_palindrome(string):
 string =string.replace("","").lower()
 d=deque(string)
 while len(d)>1:
 if d.popleft()!=d.pop():
 return False
 return True
word=input("Enter the string:")
if is_palindrome(word):
 print("",word ,"is a palindrome")
else:
 print("",word ,"is not a palindrome")
