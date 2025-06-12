**************************** Question 1 **************************************
Question: Introduction yourself based on exprience, role and project maintioned.

**************************** Question 2 Wrong 1/2 **************************************
Question: How to identify which one database is used in your project sql or no sql?
ANSWER: If my application needs strong data consistency and complex relationships, I’d go with SQL. But if it’s built for speed, scalability, and handles flexible data like logs or user-generated content, NoSQL is more appropriate. In some cases, using both can provide the best of both worlds.

Example:-
1) SQL Use case examples: Banking systems, Inventory management, ERP/CRM systems, E-commerce platforms
2) NoSQL Use case examples: Real-time analytics, IoT data ingestion, Social networks, Content management systems


******************************************** Question 3 Right 1 ********************************
Question: Defference between deepcopy and shellow copy and write example of this?
import copy

original = [[1,3,4,5], [7,8,9,10]]
shallow_copy = copy.copy(original)

print("############################# Shellow Copy ############################")
print("original", original)
print("shallow_copy", shallow_copy)
original[0][0] = 122
print("after change in original shallow_copy changed", shallow_copy)
print("original", original)
print()
print()
original_new = [[1,3,4,5], [7,8,9,10]]
deep_copy = copy.deepcopy(original_new)

print("############################# Deep Copy ############################")

print("original", original_new)
print("deep_copy", deep_copy)
original_new[0][0] = 122
print("after change in original deep_copy remain same", deep_copy)
print("original", original_new)

******************************************** Question 4 wrong 1/2 ********************************
Question: What is decorator? write decorator code using add function of 2 number

# Code:-
def decorater_func(func):
    def check_type(a, b):
        if not isinstance(a, int) and not isinstance(b, int):
            print("Both a and b are not integers.")
            return
        elif not isinstance(a, int):
            print("a is not an integer.")
            return
        elif not isinstance(b, int):
            print("b is not an integer.")
            return
        return f"sum: {func(a, b)}"
    return check_type

@decorater_func
def add(a, b):
    return a + b

# Test cases
print(add(3, 5))      # Should work output: sum:8
print(add(3, "4"))    # b is not an integer
print(add("3", 4))    # a is not an integer
print(add("3", "4"))  # Both are not integers

******************************************** Question 5.1 Right 1/2 ********************************
l = [1,2,3,4,5]

squar = list(map(lambda i: i**2, l))
print("Square of given list item", squar)  

######################## Output: Square of given list item [1, 4, 9, 16, 25]

******************************************** Question 5.2 Wrong ********************************
you have to modify this to print odd squar of given list
squar = list(map(lambda i: i**2,filter(lambda x: x%2 !=0, l)))
print("Odd item Square of given list", squar)

######################## Output: Odd item Square of given list [1, 9, 25]


******************************************** Question 6 Wrong ********************************
l = [1,2,3,4,5]

for i in l:
    l.pop()

print(l)    # Output [1, 2]   

i: Reduce the length of list on every eteration.
1 Eteration: list size : 5, remove 5 then remain list size: 4
2 Eteration: list size : 4, remove 4 then remain list size: 3
3 Eteration: list size : 3, remove 3 then remain list size: 2
__ Eteration: list size : 2, (end loop i=4 >2)


******************************************** Question 7.1 Right  ********************************
 
l = [1,2,3,4,5, [6,7,[[[[8,9, [[10]]]]]]]]

# output [1,2,3,4,5,6,7,8,9,10]
def list_flatting(l):
    res = []
    for i in l:
        if isinstance(i,list):
            res.extend(list_flatting(i))
        else:
            res.append(i)
    return res

print("Output: ",list_flatting(l))


******************************************** Question 7.2 Right ********************************
 
l = [1,2,3,(4,4),5, [6,7,[[[[8,9, [[10]]]]]]]]

# output [1,2,3,4,5,6,7,8,9,10]
def list_flatting(l):
    res = []
    for i in l:
        if isinstance(i,list):
            res.extend(list_flatting(i))
        elif isinstance(i,tuple):
            res.extend(list_flatting(i))
        else:
            res.append(i)
    return res

print("Output: ",list_flatting(l))
