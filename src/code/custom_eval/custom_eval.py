from collections import deque

def validate_input(expression):
    """
        - Evaluates if input expression is valid or not

        Validation Criteria
        --------
            - Raise Runtime exception if empty or Null input passed, incomplete expression e.g '4 + 3 - ", other chars present e.g "3 * 4 ) 1"
            - Default fallback return is 0
    """
    
    if not expression :
        raise RuntimeError("Empty or None input not allowed !!")

    #verify malformed input
    digit_exist = False
    for c in expression[::-1]:
        if c.isspace():
            continue
        elif c.isdigit():
            digit_exist = True
            break
        else:
            raise RuntimeError("Malformed Input not allowed !!") #e.g " + ", "3 + 5 -" or "5 /  "
    
    if not digit_exist: #e.g "    " -> Not allowed, but " 5  " allowed
        raise RuntimeError("Empty input not allowed !!")

def custom_eval(expression):
    """
        - Evaluate a string expression with operands (numbers) and operators
        (addition, subtraction, multiplication & division) separated by spaces
        - Algorithm: 
            - uses Stack to store previous operands after evaluation
            - initialise default prev_operand = 0 and prev_operator = +
            - iterate string from start to end:
                - if char is digit -> calculates prev_operand with consecutive digit chars
                - if char is operator('+, -, *, /') or char is last index -> evaluates the expression
                    - if prev_operator is '+,-' -> push stack with evaulated sign on prev_operand, which will used in later operations
                    - if prev_operator is '*,/' -> pop top stack value  and evaluates it with prev_operand and push it to stack
                    - always update prev_operator and prev_operand
            - after whole iteration -> return sum of stack values

        Assumption
        --------
            - Raise runtime errors like brackets or malformed input passed
            - Default fallback return is 0

        Parameters
        --------
        input: str
            expression of operators and operands separated by space
        
        Returns
        --------
        int: process string inputs and evaulates it
            Do basic evaluation on String 
    """

    validate_input(expression)
    
    size = len(expression)
    stack = deque()
    
    prev_operator = '+'
    prev_operand = 0
    
    for i in range(size):
        if expression[i].isdigit():
            prev_operand = prev_operand*10 + int(expression[i])
        
        if expression[i] in '+-*/' or i == size-1:
            if prev_operator == '+':
                stack.append(prev_operand)
            elif prev_operator == '-':
                stack.append(-prev_operand)
            elif prev_operator == '*':
                stack.append(stack.pop() * prev_operand)
            elif prev_operator == '/':
                stack.append(int(stack.pop() / prev_operand))
            
            prev_operator = expression[i]
            prev_operand = 0
        elif expression[i].isdigit() or expression[i].isspace():
            continue
        else:
            raise RuntimeError("Malformed Input not allowed !!")
    
    return sum(stack)
