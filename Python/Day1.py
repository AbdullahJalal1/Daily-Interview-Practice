#Question 1
#List vs Tuple
List=[1,20,30,4]
Tuple=(1,2,3,4)
print(List)
print(Tuple)
#add items in the end of the list
List.append(50)
print(List)

# Tuple.append(50)#Shows Error cuz tuple is immutable
# print(Tuple)

# 2. extend() - Add multiple items
List.extend([60, 70])
print(List)

# 3. insert() - Add item at a specific position
List.insert(1, 15)
print(List)

# 4. remove() - Remove a specific value
List.remove(20)
print(List)

# 5. pop() - Remove item by index
List.pop()#remove the last item of the list
print(List)

List.pop(1)#remove specific item in the list
print(List)

# 6. sort() - Sort the list
List.sort()
print(List)

# Descending order
List.sort(reverse=True)
print(List)

# 7. reverse() - Reverse the list
List.reverse()
print(List)

# 8. index() - Find the index of an item
print(List.index(30))

# 9. count() - Count How many 20 are there in the list
print(List.count(20))

# 10. copy() - Copy the list
New_List = List.copy()
print(New_List)

# 11 clear
print(New_List.clear) # Remove all items from the list


# Question 2
# == vs is
a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)

# What is a Generator?

# A generator is a special function that gives you values one at a time, 
#  instead of creating all the values at once.
# Generator
#    ↓
# Give me 1
#    ↓
# Give me 2
#    ↓
# Give me 3
#    ↓
# Give me 4

# Why use generators?
# Generators are especially useful when you have a lot of data.#
# yield means give this value then pass

def numbers():
    yield 1
    yield 2
    yield 3

for number in numbers():
    print(number)

def numbers():
    for i in range(1, 1000000):
        yield i

x = numbers()

print(next(x))
print(next(x))
print(next(x))

#List Comprehension

list=[1,2,3,4]# Simple List
print(list)

#Comprehension List 
new_list=[i for i in range(1,11)]
print(new_list)