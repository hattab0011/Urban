def all_variants(text):
    result = ['']

    for char in text:
        result += [current + char for current in result]

    for n in result:
        yield n


a = all_variants("abc")
for i in a:
    print(i)