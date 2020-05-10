import requests


r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/289.txt')
c = 0
e1 = r.text.strip().splitlines()
e2 = r.text.split('\n\n')
e3 = r.text.splitlines()
print(len(e1))
print(e1)

print(len(e2))
print(e2)

print(len(e3))
print(e3)