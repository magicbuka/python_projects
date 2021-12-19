from Stack import Stack

class Braces:
    def braces(s):
        stack = Stack()
        for brace in s:
            if brace == "(":
                stack.push(brace)
            elif stack.pop() == None:
                return False
        return stack.size() == 0
