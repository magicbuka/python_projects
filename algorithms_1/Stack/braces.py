from Stack import Stack

class Braces:
    def braces(s):
        stack = Stack()
        for brace in s:
            if brace not in "()":
                continue
            if brace == "(":
                stack.push(brace)
                continue
            else:
                if stack.pop() != None:
                    continue
                else:
                    return False
        if stack.size()==0:
            return True
        else:
            return False