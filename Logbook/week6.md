
##  Summary  

Lists allow we to group multiple values together in a specific order. Like strings, they support indexing, slicing, and looping, but unlike strings, **lists can be changed after they are created**. We can add, remove, or reorder elements using list methods such as `append()`, `extend()`, and `remove()`.

Python also provides the `del` statement, which can remove individual elements, slices of a list, or even delete the list variable entirely.

To make list creation more concise and readable, Python supports **list comprehensions**. These allow lists to be built from loops and conditions in a single line, making code shorter and easier to understand once you are familiar with the syntax.

The lecture then introduces **tuples**, which are similar to lists but **cannot be changed** once created. Tuples are typically used to group a small number of related values together, often of different data types. They are commonly accessed using **unpacking**, where each element of the tuple is assigned to a variable in one step.

Tuples play an important role in **functions**, especially when handling a variable number of arguments. When you use `*args`, Python actually packs the arguments into a tuple. Likewise, tuples (and other sequences) can be unpacked when calling a function using the `*` operator.

The lecture finishes by comparing lists and tuples, explaining when each should be used. In general, lists are best for **data that needs to change**, while tuples are best for **fixed, structured data**.

---

## Key Technologies 

### Lists

* List data type
* Mutable sequences
* Indexing, slicing, concatenation
* Iteration with `for` loops
* Common list methods:

  * `append()`, `extend()`, `insert()`
  * `remove()`, `pop()`, `clear()`
  * `sort()`, `reverse()`
  * `index()`, `count()`, `copy()`
* Mutator vs accessor methods
* `del` statement

### List Comprehensions

* Concise list creation
* Expression + `for`
* Conditional filtering with `if`
* Nested comprehensions (multiple `for` loops)

### Tuples

* Tuple data type
* Immutable sequences
* Tuple literals and constructors
* Single-element tuples (trailing comma)
* Heterogeneous data storage

### Tuple Access

* Indexing and slicing
* Tuple packing
* Sequence unpacking (multiple assignment)

### Tuples and Functions

* `*args` (variable-length argument lists)
* Tuple packing in function calls
* Sequence unpacking using `*`
* Passing tuples as positional arguments

### Lists vs Tuples

* Mutability vs immutability
* Homogeneous vs heterogeneous data
* Use cases and best practices

