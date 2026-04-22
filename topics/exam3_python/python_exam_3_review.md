# Exam 3 covers Python programming and Ethics

* Students may use a 1-page (8.5” by 11” front/back) help guide on the exam
* Review class notes, examples on the course website, book, and Python assignments

## Topics
* Current Ethical Issues (briefly describe several current examples)
* Ethical Analysis (facts, issues, people affected, consequences, faith/values) note: be able to list these questions that should be addressed  
* IPO (Input, Output, Processing) for planning, recognize flowchart symbols
* comments # and """
* valid variable names (start with a letter, then letter, number, underscore)
* variable types number int (7, 2700, -8), float (3.14, -98.6), str ("abc", ‘abc’, "46750")
* use print to display text and variables on a single line, end=””
* use print formatting f”text {variable}” including formatting to one {v:.1f} or two{v:.1f} decimal places
* arithmetic operations (*, /, + -), order of precedence ie. parenthesis, exponents, mult/div, add/sub
* input values from keyboard using input statement and convert to int or float  
* if, else, relational operators (<, >, <=, >=, ==, !=), and, or)  
* generate random numbers 0 to N, 1 to N
* while loop, repeat code N times, sentinel loop  
* lists [], empty list, index list[n], append
* len, sum, min, max
* loop to print all items in a list

## Sample Questions


### 1. Current Ethical Issues
**Question:** Briefly describe several current ethical issues.

**Sample Answer:**
- AI bias in decision-making systems  
- Data privacy and tracking by companies  
- Use of AI in education (cheating concerns)  

---

### 2. Ethical Analysis
**Question:** What questions should be addressed in an ethical analysis?

**Sample Answer:**
- What are the **facts**?  
- What are the **issues**?  
- Who is **affected**?  
- What are the **consequences**?  
- What **values/faith principles** apply?  

---

# Concepts

### 3. IPO Model
**Question:** What is an IPO chart?

**Sample Answer:**
An IPO chart describes:
- **Input** – data received  
- **Processing** – calculations/logic  
- **Output** – results displayed  

It helps plan programs before coding.

---

# Python Basics

### 4. Variable Names
**Question:** Which is NOT valid?

a. total1  
b. 1total  
c. total_score  
d. totalScore  

**Answer:** **b. 1total** (cannot start with a number)

---

### 5. Comments
**Question:** Which is a valid single-line comment?

a. //comment  
b. /* comment */  
c. #comment  
d. *** comment  

**Answer:** **c. #comment**

---

### 6. What will print to the screen when the following Python code is executed?
```python
a = 10
b = 20
print("a + b")
print(a + b)

amount = 7.4589
print(f"amount = ${amount:.2f}")
````

**Answer:**

```
a + b
30
amount = $7.46
```

---

### 7. Order of Operations

**Question: What value is assigned to x?**

```python
x = 40 - 20 / 4 * 5 + 3
```

**Answer:**

* 20 / 4 = 5
* 5 * 5 = 25
* 40 - 25 + 3 = **18**

---

### 8. What will print to the screen when the following Python code is executed?

```python
temp = 2
temp = temp + 1
print(temp / 2)

temp = temp + 3
print(temp)
```

**Answer:**

```
1.5
6
```

---

### 9. Boolean Logic #1

**Question: What value will be displayed by the following code, given: a=10, b=20, c=30?**

```python
if a > b or b < c:
     print("True")
else:
     print("False")
```

**Answer:** **True**

---

### 10. Boolean Logic #2

**Question: What value will be displayed by the following code, given: a=10, b=20, c=30?**

```python
if c == 30 and b > c:
     print("True")
else:
     print("False")
```

**Answer:** **False**

---

### 11. Program Comments

**Question:** What comments should be included at the beginning of every program?

**Sample Answer:**

* program name ie. exam3.pay
* Author name ie. Norman Forester
* Date ie. April 30, 2026
* Purpose/Description of program ie. program calculates an average grade

---

# Coding Questions

### 12. Dessert Logic (individual ifs)

**Question: Use individual If statements to determine dessert choices.**

```python
choice = 4
dessert = "undefined"

if choice == 1 or choice == 2 or choice == 3:
    dessert = "Cookie"

if choice == 4 or choice == 5:
    dessert = "Cake"

if choice == 6 or choice == 7:
    dessert = "Pie"

print( "dessert is", dessert )
```

---

### 13. Temperature Program

```python
temp = float(input("Enter temperature: "))

if temp > 32.0:
    print(f"{temp} is above freezing")
else:
    print(f"{temp} is freezing")
```

---

### 14. Random Number (0–3)

```python
from random import randint
x = randint(0, 3)
```

---

### 15. Random Number (17–19)

```python
x = randint(17, 19)
```

---

### 16. Random Word

```python
from random import randint

r = randint(1, 3)

if r == 1:
    word = "go"
if r == 2:
    word = "fight"
if r == 3:
    word = "win"

print(word)
```

---

### 17. While Loop Output

```python
count = 0
while count < 4:
    print(count)
    count = count + 2
```

**Answer:**

```
0
2
```

---

### 18. Countdown

```python
count = 5000
while count >= 1:
    print(count)
    count = count - 1
```

---

### 19. Repeat Name

```python
count = 1
while count <= 3000:
    print("Norman Forester")
    count = count + 1
```

---

### 20. Sentinel Loop

```python
total = 0

num = int(input("Enter number (-1 to stop): "))

while num != -1:
    total = total + num
    num = int(input("Enter number (-1 to stop): "))

print("Total =", total)
```

# Python Lists Review

## 21. Creating Lists

### Question
Create a list named `numbers` that contains the values 5, 10, and 15.

### Answer
```python
numbers = [5, 10, 15]
````

---

### Question

Create an empty list called `data`.

### Answer

```python
data = []
```

---

## 22. Indexing

### Question

Given the list below, what value is stored in `x`?

```python
colors = ["red", "green", "blue"]
x = colors[1]
```

### Answer

```
green
```

---

### Question

What index would you use to access the first item in a list?

### Answer

```
0
```

---

## 23. Append

### Question

Write code to add the value `25` to the list `numbers`.

### Answer

```python
numbers.append(25)
```

---

## 24. List Functions

### Question

Given the list below, what will each statement return?

```python
values = [4, 7, 2, 9]
```

* `len(values)` = ______
* `sum(values)` = ______
* `min(values)` = ______
* `max(values)` = ______

### Answer

```
len(values) = 4
sum(values) = 22
min(values) = 2
max(values) = 9
```

---

## 25. Loop Through a List

### Question

Write a loop to print all items in the list `fruits`.

```python
fruits = ["apple", "banana", "cherry"]
```

### Answer

```python
i = 0
while i < len(fruits):
    print( fruits[ i ] )
    i = i + 1
```


-- end --
