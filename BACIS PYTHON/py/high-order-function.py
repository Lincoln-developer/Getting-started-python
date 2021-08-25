"""
High order function is a function that takes in another function as an argument
or returns a function
these include the map() and filter() built in functions

"""
#map()
l = [2,3,4,5]
mylist = list(map(lambda a : a *3, l))
print(mylist)

#filtering items in list using the filter()
filteredlist = list(filter(lambda a: a <= 4,l))
print(filteredlist)

words = str.split('the longest word in here')
sortedword = sorted(words,key=len)
print(sortedword)


