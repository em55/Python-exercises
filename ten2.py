a = ['a','b',['c','d',['e','f']],['r','yolo!']]

def combine(l):
    return "".join(c if type(c) is str else combine(c) for c in l )
    
print list(combine(a).upper())


