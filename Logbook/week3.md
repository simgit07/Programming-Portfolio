
##  Summary 
This lecture explains how programs **make decisions and repeat actions**, which is what gives code its “intelligence”.

Up to now, programs have mostly run **line by line**, but real programs need logic — they need to **choose** what to do and **repeat** tasks when necessary. This is done using **control statements**.

Programs make decisions using **Boolean expressions**, which always evaluate to either **True or False**. These expressions compare values (like checking if one number is bigger than another) and are used to decide which parts of the code should run.

To make decisions, Python uses **if, elif, and else statements**. These allow programs to execute different code depending on conditions, such as a user’s age or input. When decisions get more complex, **logical operators** like `and`, `or`, and `not` are used to combine multiple conditions.

Python also provides **membership testing**, which lets a program check whether something exists inside a list or a string, such as checking if a name appears in a list or if a word appears in a sentence.

For short decisions where one of two values must be chosen, Python offers the **ternary operator**, which is a compact, single-line alternative to an `if…else` statement.

To repeat actions, Python uses **loops**. A **while loop** repeats as long as a condition remains true, while a **for loop** repeats over a sequence of values, such as a list or a range of numbers. The `range()` function is commonly used to control how many times a loop runs.

Loops can be controlled using **break** (to stop a loop early) and **continue** (to skip to the next loop cycle). Python also allows an **else block on loops**, which runs only if the loop finishes normally without breaking.

Finally, the lecture introduces **nested control statements**, where one decision or loop exists inside another. While powerful, too much nesting can make code difficult to understand and inefficient.

Overall, this lecture shows how **logic, decisions, and repetition** turn simple code into useful programs.

---

## Key Technologies 

### Core Programming Concepts

* Algorithms
* Control flow
* Sequence, selection, iteration
* Boolean logic

### Decision Making

* `if`, `elif`, `else`
* Ternary operator
* Relational operators (`<`, `>`, `==`, `!=`, etc.)
* Logical operators (`and`, `or`, `not`)

### Data Testing

* Membership testing (`in`, `not in`)
* Truthy and falsy values
* Relational operator chaining

### Iteration (Loops)

* `while` loops
* `for` loops
* `range()` function

### Loop Control

* `break`
* `continue`
* `else` with loops

### Code Structure

* Indentation-based code blocks
* Nested control statements

