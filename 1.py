def is_item_here(item, *args):
    res =[]
    for i in args:
        if item in i:            
            res.append('True')
        else: res.append('False')
    return res       
list_str = ['cotton', 'cover', 'cat', 'dog']
rez = is_item_here('c', 'cotton', 'cover', 'cat')
print(rez)   
#for i in list_str:
#    print(i)
#   print('c' in i)

