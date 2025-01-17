# Task_1
tpl = (1, 3, 3, 5, 3)
element = 3
count = tpl.count(element)
print(f"1-task: {element} element {count} marta takrorlangan.")

# Task_2
inx_elmt = tpl.index(element)
print(f"2-task: {element} elementi birinchi {inx_elmt}-indexga joylashgan")

# Task_3
noyb = set(tpl)
print("3-task: Takrorlanuvchi elementlar:")
for item in noyb:
    count = tpl.count(item)
    if count > 1:
        print(f"{item} elementi {count} marta takrorlangan.")

# Task_4
mst_elmt = max(noyb, key=tpl.count)
mst_count = tpl.count(mst_elmt)
print(f"4-task: Eng ko'p takrorlangan: {mst_elmt}, {mst_count} marta.")