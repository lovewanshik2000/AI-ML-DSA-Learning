******************************************* 18-JUNE -2025 *************************************************
from collections import defaultdict

records = [
    {"id": 1, "name": "Alice", "department": "HR"},
    {"id": 2, "name": "Bob", "department": "Finance"},
    {"id": 3, "name": "Charlie", "department": ["HR", "Finance"]},
    {"id": 4, "name": "David", "department": "IT"},
    {"id": 5, "name": "Eve", "department": "Finance"},
]

count = defaultdict(int)

for i in records:
    dept = i["department"]
    if isinstance(dept, list):
        for j in dept:
            count[j] += 1
    else:
        count[dept] += 1

print(dict(count))
    

**************************************************************************************************************
a = 10
b = 20   
b = a #10
c = a+b  # 10 +10 = 20
d = b+c   #  10 + 20 = 30

print(a,b,c,d) 

# OUTPUT: 10,10, 20, 30
***************************************************************************************************************

var = 10,
print(var, type(var))


OUTPUT: tuple

1. What is middelware
2. What is request and response model in fastapi.
3. What is pydantic?
4. Why use models and schemas?
5. Deffirence between list and tuple?
6. What is GIL?
7. What is supervisor in deployment?
8. What is pull in git and how it works?
9. How to change fastapi docs Default name?
10. Constructor and Destructor in python and which keyword is used for this?
11. write a query in fastapi to remove all records that is devided by devisible by 5.
12. 