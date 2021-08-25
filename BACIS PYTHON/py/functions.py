def greeting(language) :
    if language == 'eng':
       return 'Hello world, this is english language'
    elif language == 'fr':
        return 'Bonjour le monde'
    else: return 'undefined'

l = [greeting('eng'),greeting('fr'),greeting('ger')]
print(l[1])
print(l[0])
print(l[2])

#Setting functions as arguments to another functions
def call(f):
    lang = 'eng'
    return (f(lang))

print(call(greeting))

#second function
def programmingLanguages(computerLang) :
    if computerLang == 'python':
        return 'Python is a high programming language'
    elif computerLang == 'javascript':
        return 'Javascript is mainly for web development'
    else: return 'No language is popular than these two'
#passing the function object into a list
codingList = [programmingLanguages('python'),programmingLanguages('javascript'),
programmingLanguages('c++')]
#printing result statements according to indecies
print(codingList[0])
print(codingList[1])  
print(codingList[2]) 
#passing a function as an argument to another function
def another(func) :
    cl = 'python'
    return(func(cl)) 

print(another(programmingLanguages))



