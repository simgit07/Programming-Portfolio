
## Summary



So far, we've been using a few **built-in functions** like `print()` and `input()`, but Python actually provides **many more functions** through its **standard library**. These extra functions are stored in **modules**, and we must **import** them before use. we can import an entire module, specific functions, or (less recommended) everything at once. Importing only what we need keeps programs cleaner and easier to read.

Besides functions, modules can also provide **special data types**, such as `Decimal`, which is useful for accurate financial calculations. This avoids the rounding errors that occur with floating-point numbers.

The lecture then explains how to **define your own functions** using the `def` keyword. Functions can accept input values (parameters), perform operations, and optionally **return a result**. Variables inside a function are **local**, meaning they only exist while the function is running.

Good functions include **docstrings**, which are short descriptions explaining what the function does. These help both programmers and documentation tools understand your code.

Functions can be made more flexible using **default arguments**, allowing some parameters to be optional, and **keyword arguments**, which allow arguments to be passed by name instead of position. This improves readability and makes function calls clearer.

Some functions can accept a **variable number of arguments**, like `print()`. This is done using `*args`, which collects arguments into a tuple. Python also supports **arbitrary keyword arguments** using `**kwargs`, allowing functions to accept named arguments that weren’t explicitly defined.

Finally, the lecture introduces **lambda expressions**, which are small, anonymous functions written on a single line. These are especially useful when passing simple functions into other functions, such as when sorting data. While they may seem confusing at first, they are powerful tools in Python programming.

Overall, functions are a core building block in Python, helping make code **modular, reusable, readable, and efficient**.

---

## Key Technologies 

### Functions & Modularity

* Built-in functions
* User-defined functions
* Function calls
* Return values
* Local vs global variables

### Imports & Libraries

* `import module`
* `from module import function`
* Python Standard Library
* Avoiding namespace pollution
* Importing constants and data types

### Data Types from Modules

* `Decimal` type
* Floating-point precision issues
* Monetary calculations

### Function Design

* `def` keyword
* Formal parameters vs actual arguments
* Docstrings
* Returning `None`

### Function Arguments

* Positional arguments
* Default arguments
* Keyword arguments
* Argument order rules

### Variable-Length Arguments

* `*args` (variable positional arguments)
* Tuples
* Iterating over arguments

### Arbitrary Keyword Arguments

* `**kwargs`
* Dictionaries
* Flexible function interfaces

### Lambda Expressions

* Anonymous functions
* `lambda` keyword
* Single-expression functions
* Passing functions as arguments
* Using lambdas with `sorted()` and `key=`

