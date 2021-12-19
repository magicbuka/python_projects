import operator
from Stack import Stack
from Stack_reverse import Stack_reverse

class Postfix:
    def get_operator(op):
        return {'+': operator.add,
                '*': operator.mul}[op]

    def postfix(s):
        stack_main = Stack_reverse()
        stack_num = Stack()
        for elem in s:
            if elem != ' ':
                stack_main.push(elem)
        while stack_main.size() != 0:
            elem = stack_main.pop()
            if elem not in '*+=':
                stack_num.push(elem)
            elif elem not in '=':
                y = int(stack_num.pop())
                x = int(stack_num.pop())
                result = Postfix.get_operator(elem)(x, y)
                stack_num.push(result)
            else:
                return stack_num.pop()
        return stack_num.pop()