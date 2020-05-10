def coding(code, key, string, B):
    code_dict = {}
    key_dict = {}
    result = ''
    for i in range(len(key)):
        key_dict[key[i]] = code[i]
        code_dict[code[i]] = key[i]

    if B:
        for i in string:
            if i not in key_dict.keys():
                result += '?'
            else:
                result += key_dict[i]
    else:
        for i in string:
            if i not in code_dict.keys():
                result += '?'
            else:
                result += code_dict[i]
    return result


a = 'abcd'
b = '*d%#'
a1 = 'abacabadaba'
b1 = '*d*%*d*#*d*'
result_shifr = ''
result_key = ''

ashifr = {}
akey = {}



for i in range(len(a)):
    ashifr[a[i]] = b[i]
    akey[b[i]] = a[i]

for i in a:
    result_shifr += ashifr[i]

for i in b:
    result_key += akey[i]

'''for i in range(0,len(b)):
    for key in ashifr.keys():
        if b[i] == ashifr[key]:
            print(key, end='')'''

#print(a)
#print(b)

print(coding(a, b, a1, 0))
#print(result_shifr)
#print(result_key)

