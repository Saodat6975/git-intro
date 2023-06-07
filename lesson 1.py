def add_dots(string):
    return '.'.join(string)

def remove_dots(string):
    return string.replace('.', '')

    
print(add_dots('test'))
print(remove_dots('M.a.h.m.u.d'))