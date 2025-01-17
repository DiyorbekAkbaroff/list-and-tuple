#TASK_1
tpl = (1, 2, 3, 4)
print("1-task:", tpl)

#TASK_2
try:
    tpl[4] = 5  # ile ozgarmasligi ucn try exceptdan foydalaniwga qaror qildm
except TypeError as Xato:
    print("2-task: ile ozgarmas malumot qoshilmedi")
    print("Xato tafsiloti:", Xato)

#TASK_3
tpls2 = [(1, 2, 3), (4, 5, 6), (7, 8, 3), (9, 3, 11), (12, 13, 3)]
print("Qaysi sonni qidirmoqchisiz: ")
srch = int(input("Son kiriting: "))
res = False

for i in tpls2:
    if srch in i:
        print(f"3-task: {srch} topildi:", i)
        res = True

if True:
    print(f"3-task: {srch} topilmadi")