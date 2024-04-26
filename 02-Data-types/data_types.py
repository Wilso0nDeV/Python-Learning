#Data Types Basics

#!Funcion 'type()' : It allows us to know the type of data 

#!Integer : -3,-2,-1, 0 , 1, 2, 3 ...

print(type(-3)) #int
print(type(3))  #int
print(type(0))  #int


#!Float : -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...


print(type(-3.5)) #float
print(type(3.5)) #float
print(type(0.0)) #float

#!Complex: 1 + 3j, 2 + 4j
print(type(1 + 3j)) #complex

#!String : 
"""Collection of one o more characters under a single or double quote, 
If a string is more than one sentence then we use a triple quote."""


print(type('Hola mundo')) #str    
print(type("Hola mundo")) #str    
print(type('''
        Hola
        Como estas
'''))                   #str

#!Booleans : true o false
print(type(True)) #bool
print(type(False)) #bool

#List : Python list is an ordered collection which allows to store different data type items

print(type([0,1,2,3])) #list of numbers
print(type(['Banana', 'Orange', 'Mango', 'Avocado'])) #list of string
print(type(['Banana', 10, False, 9.81])) #list of string, integer, boolean and float


#!Dictionary
#A Python dictionary object is an unordered collection of data in a key value pair format.

#This is a Dictionary
print({
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
})

print(type({
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
})) #dict

#!Tuplas
"""A tuple is an ordered collection of different data types like list
but tuples can not be modified once they are created. They are immutable."""

#This is a Tuple
('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya')# Names

print(type(('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya'))) # tuple

#!Set
"""
A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. 
Like in Mathematics, set in Python stores only unique items."""

#This is a Set
print({2, 4, 3, 5,1}) #set decides how to display the order
print(type({2, 4.4, 3, 5})) #set