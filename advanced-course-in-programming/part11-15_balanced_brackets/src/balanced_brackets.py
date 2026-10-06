
def balanced_brackets(my_string: str):
    allowed="[]()"
    my_string="".join([char for char in my_string if char in allowed])
    if len(my_string) == 0:
        return True
    if not ((my_string[0] == '(' and my_string[-1] == ')') or (my_string[0] == '[' and my_string[-1] == ']')):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])