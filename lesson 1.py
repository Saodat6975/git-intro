def add_dots(string):
    return '.'.join(string)

def remove_dots(string):
    return string.replace('.', '')

    
print(add_dots('test'))
print(remove_dots('s.a.odat'))