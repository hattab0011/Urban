calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    str_info = len(string), string.upper(), string.lower()
    return tuple(str_info)

def is_contains(string,array):
    count_calls()
    string_lower = string.lower()
    array_lower = [s.lower() for s in array]
    if string_lower in array_lower:
        return True
    else:
        return False

is_contains('Привет',['Привет', 'Hello'])
string_info('Привет')
string_info('Array')
string_info('Thunder')

print(calls)