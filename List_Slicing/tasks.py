print("TASK-01") #TASK01
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("2 va 7-elementlar orasi:", lst[1:7])

print("TASK-02") #TASK02
print("Har uchinchi element:", lst[::3])

print("TASK-03") #TASK03
nw_lst = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
print(nw_lst)

print("TASK-04") #TASK04
new_list = nw_lst[:3] + nw_lst[-3:]
print("Yangi list:", new_list)

print("TASK-05") #TASK05
print("listni teskari tartibi:", new_list[::-1])