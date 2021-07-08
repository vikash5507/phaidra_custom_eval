import sys

from custom_eval.custom_eval import custom_eval


def process(inputArg):
    """
        process input text File or String expression to read each evaluation string instruction

        Parameters
        --------
        inputArg: str
            input file path or string expression
        
        Returns
        --------
        void: process string inputs and evaulates it and print it to console
    """
    
    if inputArg.split('.')[-1] not in ["txt", "text"]:
        result = process_input(inputArg)
        print(result)
        return result

    try:
        with open(inputArg, 'r') as reader:
            for line in reader:
                try:
                    ### process each input ###
                    result = process_input(line)
                    print(result)
                except:
                    print("Error: Not a valid operation!!")
    except FileNotFoundError as fnfError:
        print("File Not found!!", fnfError)

def process_input(expression):
    """
        take string expression as input and return custom_eval module result
    """
    return custom_eval(expression)


def main():
    """
        Main function to execute on input. Input can be file(.txt, .text) or string expression itself
    """

    if len(sys.argv) < 2:
        raise RuntimeError("No Input given. Nothing to process !!") 
    
    inputArg = sys.argv[1]
    try:
        process(inputArg)
    except:
        raise RuntimeError

if __name__ == "__main__":
    ## Run instuction or command
    main()