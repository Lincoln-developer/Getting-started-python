#sets are unordered and unindexed
myset = {'banana','orange','apple','maize','boy'}
myset2 = {'banana','orange','jackfruit','ovacado'}
#add item to set
myset.add('carrot')
print(myset)
myset.remove('boy')
print(myset)
myset.union(myset2)
print(myset)
myset.update(['hobbies','coding','eating'])
print(myset)


