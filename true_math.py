from math import inf
def divide(first, second):
    if second == 0:
        return inf
    else:
        return int(first/second)

if __name__ == '__main__':
    result = divide(4, 2)
    print(result)