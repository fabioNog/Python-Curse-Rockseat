def filter_list(l):
    newl = []
    for x in l:
        if not isinstance(x, str):
            newl.append(x)
    return newl

print(filter_list([1, 2, 'a', 'b']))