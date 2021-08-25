#dictionaries are unordered, changeable and indexed

mydictionary = {
    'name':'ang lincoln',
    'age':'21',
    'height':'tall',
    'skin color':'dark skinned',
    'residence':'Nsambya',
    'tribe':'lugbara',
    'nationality':'Ugandan'
}
print(mydictionary)

#accessing dictionary items by refering to the key name and get method
x = mydictionary['age']
print(x)
y = mydictionary.get('nationality')
print(y)
#changing the value of the key in the dictionary
mydictionary['name'] = 'angufibo tonny lincoln'
print(mydictionary)
#looping through the dictionary
for x in mydictionary:
    print(x)

for x in mydictionary:
    print(mydictionary[x])