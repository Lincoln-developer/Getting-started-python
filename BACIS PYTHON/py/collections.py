#these are basically arrays

#lists:these are ordered and changeable collection data type

todo_list = [
    "code",
    "eat breakfast",
    "sleep",
    "play",
    "visit friend"
]

print(todo_list)
#access list items
print(todo_list[1])
#change list items
todo_list[3] = 'eat lunch'
print(todo_list)

#looping through the list
for x in todo_list:
    print(x)

#determining the length of the list    
print(len(todo_list))
#adding an item to the end of list
todo_list.append('code again')
print(todo_list)
#add at specified index
todo_list.insert(0, 'code addict')
print(todo_list)
#remove item  at specified index
del todo_list[3]
print(todo_list)

#Nesting lists
items = [['rice',2.4,8],['flour',1.9,4],['water',6.9,10] ]
for item in items:
    print('product: %s price: %.2f Quality: %i' % (item[0],item[1],item[2]))