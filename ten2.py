def combine(s):
    i=0
    for i in range(len(s)):
        if type(s[i]) is list:
            combine(s[i])
        else:
        
            big_list.append(s[i])
    return big_list

big_list = []
a = ['a','b',['c','d',['e','f']],['r','yolo!']]
combine(a)
print big_list

print [x.upper() for x in big_list]

