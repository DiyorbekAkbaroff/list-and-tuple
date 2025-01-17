# Bu tasks02.py faylida task03, task04, task05 fayllari bajarilgan

lst = [-3, -2, -1, 0 , 1, 2, 3, 4, 5, "HELLO", "WORLD", "QALE", "ISHLAR"]

lst2 = []
lst3 = []

for i in lst:
    if type(i) == int and i < 0:
        continue
    lst2.append(i)

for i in lst2:
    if type(i) == str and i.isupper():
        lst3.append(i.lower())
    else:
        lst3.append(i)

print(lst3)