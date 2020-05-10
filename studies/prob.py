import re
from urllib.request import urlopen
html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')
s = str(html)
a =[]
d ={}
r = set()
a = re.findall(r'(?<=<code>).*?(?=<\/code>)', s)
for i in a:
    d[i] = a.count(i)
for k, v in d.items():
    if v == max(d.values()):
        r.add(k)
for i in sorted(r):
    print(i, end=' ')