def SubString(main_str,sub_str):
    n = len(main_str) - len(sub_str) + 1
    count = 0
    for i in range(n):
        if(main_str[i:len(sub_str)+i] == sub_str):
            count = count+1
    return count

main_str = input()
sub_str = input()
result = SubString(main_str,sub_str)
print(result)