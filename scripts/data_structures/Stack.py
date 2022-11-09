from collections import deque

# Custom Stack class
class Stack:
    def __init__(self):
        self.stack = deque()
        
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def squint(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def length(self):
        return len(self.stack)


# The below functions were used to implement parenthesis matching.
def isMatch(a, b):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    return match[a] == b

def isBalanced(string):
    stack = Stack()
    for char in string:
        if char=='(' or char=='{' or char=='[':
            stack.push(char)
        if char==')' or char=='}' or char==']':
            if stack.length() == 0:
                return False
            if not isMatch(char, stack.pop()):
                return False
    
    return stack.length() == 0


if __name__ == '__main__':
    stack = Stack()
    stack.push('A stack')
    stack.push('demo from')
    stack.push('ifunanyaScript')
    print(stack.squint())
    print(stack.stack)
    stack.pop()
    print(stack.stack)
    print('___________________________')
    print(isBalanced('({[Parenthesis Matching from ifunanyaScript]})'))
    print(isBalanced('{]There is definitely a glitch here}'))
    print(isBalanced('({[({[]})]})'))
    print(isBalanced('[{Machine Learning Engineer)}]'))


# ifunanyaScript