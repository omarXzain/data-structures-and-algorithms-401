
def multi_bracket_validation(strings):

    arr = []
    obj = { '(':')', '[':']', '{':'}' }

    for x in strings:
        if (x == '(' or x == '{' or x == '['):
            arr.append(x)

        else:
            item = arr.pop()
            if x != obj[item]:
                return False

    if len(arr) != 0:
        return False
    
    return True

print(multi_bracket_validation('(){}'))
print(multi_bracket_validation('({()}'))
print(multi_bracket_validation('({())'))
print(multi_bracket_validation('({())))'))
print(multi_bracket_validation('({()]'))
print(multi_bracket_validation('({()})'))