operator=set(["+","","*","/","(",")","^"])
priority={'+':1,'-':1,'*':2,'/':2,'^':3}
def infix_to_postfix(expression):
 stack=[]
 output=''
 for ch in expression:
 if ch not in operator:
 output+=ch
 elif ch=='(':
 stack.append('(')
 elif ch==')':
 while stack and stack[-1]=='(':
 output+=stack.pop()
 stack.pop()
 else:
 while stack and stack[-1]!='(' and priority[ch]<=priority[stack[-1]]:
 output+=stack.pop()
 stack.append(ch)
 while stack:
 output+=stack.pop()
 return output
expression=input("enter the infix expression:")
print("infix expression:",expression)
print("infix to postfix expression:",infix_to_postfix(expression))
