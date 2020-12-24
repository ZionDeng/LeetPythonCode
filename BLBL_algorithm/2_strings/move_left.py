# abcdef -> cdefab
# (X'Y')' = YX 


def move_left(s,index):
    '''
    s: string to remove
    index: length to remove
    return: result 
    '''
    x_dot = s[:index][::-1]
    y_dot = s[index:][::-1]
    return (x_dot + y_dot)[::-1]

print(move_left('abcdef',2))