import requests

url = 'https://stepic.org/media/attachments/course67/3.6.3/'
t = '699991.txt'
r = requests.get(url+t)
c = 1
t = r.text

while t[0] != 'W':
    print(t, c)
    r = requests.get(url+t)
    t = r.text
    c += 1
print(t)
print(c)