"""
Write a function to evaluate (a simple subset of) arithmetic expressions.

   input characters: ()1234567890+*
   valid input: only single digits
                only well balanced brackets
                brackets around EVERY binary operation!
   invalid input: raise SyntaxError()

Examples:

   my_eval("5")  =>  5
   my_eval("(5+1)")  =>  6
   my_eval("(5+(3*2))")  =>  11
   my_eval("((1+2)+(3*2))")  =>  9
   my_eval(" ((1+(3+8)) + ((7+8)*2)) ")  =>  42
   my_eval("5+3*2")  =>  SyntaxError
   my_eval("5.3+i")  =>  SyntaxError

"""


def extract(s: str):
    depth = 0
    for i, char in enumerate(s):
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        else:

            if depth == 0 and char in ['*', '+']:
                first_operand = s[:i]
                opt = s[i]
                second_opt = s[i + 1:]
                return first_operand, opt, second_opt


def my_eval(s: str) -> int:
    """
    :param s:
    :return:
    """
    # (1) First write some assertions to ensure that s is indeed a valid input
    try:
        # (2) If it is a valid int, then return int(s).
        return int(s)
    except ValueError:
        # (3) We have at least a single ()
        assert ('(' in s) and (')' in s), s
        if len(s) == 5:
            # (3.1) If we have a single (), then we have a single arithmetic opt. extract operands and operators.
            first_operand, opt, second_operand = s[1:-1]
        else:
            first_operand, opt, second_operand = extract(s[1:-1])

        if opt == '*':
            def opt(a, b):
                return a * b
        else:
            def opt(a, b):
                return a + b

        return opt(my_eval(first_operand), my_eval(second_operand))


print(my_eval("(5+1)"))
print(my_eval("(5+(3*2))"))
print(my_eval("((1+(3+8))+((7+8)*2))"))
