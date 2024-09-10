def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        function_name = function.__name__
        result[function_name] = function(int_list)

    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))