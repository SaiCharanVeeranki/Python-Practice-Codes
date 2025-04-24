# PYTHON -----> Python

# input_str = input()

def SwapCase(input_str):
    converted_str = ''
    for i in input_str:
        if i.islower():
            converted_str = converted_str + i.upper()
        else:
            converted_str = converted_str + i.lower()
    return converted_str

res = SwapCase('Python234')
print(res)
    