#TASK_1
text = "Hello World!"
lst = list(text)
print(lst)

#TASK_2
lst2 = ''.join(lst)
print("Birlashgani: ", lst2)

#TASK_3
text = "Python programming is amazing!"

sozlar = text.split()
print("Sozlar:", sozlar)

frst = []
for word in sozlar:
    frst.append(word[0])
    
result = ''.join(frst)
print("birinchi harflari:", result)