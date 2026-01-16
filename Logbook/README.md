# WEEK 1
1. A computer program is a sequence of instructions that takes input, processes it, and produces output.
2. Programming languages evolved from machine code (1GL) to high-level languages like Python (3GL) to make programming easier and more portable.
3. Python is a popular, easy-to-learn, interpreted third-generation language used in education and industry.
4. Python can be used interactively with the interpreter (REPL) or through files and IDEs for larger programs.
5. Python relies heavily on libraries, which provide pre-written code to perform complex tasks efficiently.
6. Expressions are fundamental in Python and use operators such as +, −, *, /, **, with defined operator precedence.
7. Errors are a normal part of programming and include syntax errors, logical errors (bugs), and runtime errors, which must be identified and fixed through careful reading of error messages and testing.


# WEEK 2
1. **Variables** store values for later use and are identified by meaningful, case-sensitive names made of letters, digits, and underscores.
2. **Assignment (`=`)** stores the evaluated right-hand expression into a variable, and variables can be updated using normal or augmented assignment (e.g. `+=`, `-=`).
3. Python uses **dynamic typing**, meaning a variable’s data type depends on its most recent value (e.g. `int`, `float`, `bool`, `str`).
4. **Functions** like `print()`, `type()`, `len()`, and `input()` execute predefined code; `input()` always returns a string and may require type conversion.
5. **Strings** can be created using single, double, or triple quotes and support escape sequences, indexing, slicing, and concatenation, but they are **immutable**.
6. **Lists** are ordered collections that can store multiple values, support indexing and slicing, and unlike strings are **mutable**.
7. Lists can be **mutated** using methods like `append()`, augmented assignment, and slice assignment, and their size can be checked using `len()`.

If you want, I can also turn this into **exam answers**, **flashcards**, or **practice questions**.

# WEEK 3
1. Programs implement **algorithms** using three core ideas: **sequence**, **selection**, and **iteration**.
2. **Boolean expressions** evaluate to `True` or `False` and are built using relational operators (e.g. `<`, `==`, `!=`) and logical operators (`and`, `or`, `not`).
3. **Selection** is implemented using `if`, `elif`, and `else` statements to decide which code blocks execute.
4. Python supports **membership testing** with `in` and `not in`, and non-Boolean values can act as conditions (`0`/empty = False, non-zero/non-empty = True).
5. The **ternary operator** provides a concise way to return one of two values based on a condition (`a if condition else b`).
6. **Iteration** is achieved using `while` loops (condition-based repetition) and `for` loops (iterating over sequences or ranges).
7. Loops can be controlled using **`break`**, **`continue`**, optional **loop `else` clauses**, and can be **nested**, though deep nesting should be avoided for readability and performance.

# WEEK 4
1. Python provides many **built-in functions** and thousands more via modules, which must be **imported** before use.
2. Functions and data-types can be imported from modules using `import module` or `from module import name`, but importing only what is needed is best practice.
3. Programmers can **define their own functions** using `def`, with a name, parameters, an indented code block, and usually a **docstring**.
4. Functions may **return values** using `return`; if no return statement is used, the function returns `None`.
5. Functions can use **default arguments** and **keyword arguments**, allowing flexible and readable function calls.
6. Python supports **variable-length argument lists** (`*args`) and **arbitrary keyword arguments** (`**kwargs`) for functions that accept many inputs.
7. **Lambda expressions** allow small, anonymous functions to be created and used as values, often passed as arguments to other functions.

# WEEK 5
1. Python programs can be written in **.py files** called scripts, which are executed by passing the filename to the Python interpreter.
2. Scripts differ from interactive mode because expressions do not automatically print results; explicit `print()` statements are required.
3. Scripts can receive **command-line arguments**, which are accessed using the `sys.argv` list.
4. Any `.py` file can also act as a **module**, allowing its functions, variables, and types to be reused in other programs.
5. Modules can be imported in different ways (`import module`, `import module as alias`, `from module import name`), each affecting how names appear in the local namespace.
6. When importing a module, Python searches for it using the **module search path** (`sys.path`), which includes the current directory and other configured locations.
7. The special variable **`__name__`** allows a file to behave differently when run as a script (`"__main__"`) or when imported as a module.

# WEEK 6
1. **Lists** are ordered, mutable sequences that support indexing, slicing, iteration, and modification using methods such as `append()`, `extend()`, and `remove()`.
2. **List methods** are functions associated with the list type; most mutate the list and return `None`, while accessor methods like `index()` and `count()` return values without changing the list.
3. The `del` statement can remove individual elements, slices, or entire list variables.
4. **List comprehensions** provide a concise way to create lists programmatically using expressions with `for` loops and optional `if` conditions.
5. **Tuples** are ordered sequences similar to lists but are **immutable**, meaning their contents cannot be changed after creation.
6. Tuple elements can be accessed by **indexing, slicing, or unpacking**, and tuples are commonly used to group small sets of heterogeneous values.
7. Tuples are widely used in **function arguments**, supporting variable-length argument lists (`*args`) and sequence unpacking during function calls.

# WEEK 7
1. **Sets** store unordered collections of **unique, immutable values**, meaning duplicates are not allowed and elements have no index or position.
2. Sets support **membership testing** and mathematical operations such as **union, intersection, difference, and symmetric difference**, using operators or methods.
3. Sets are **mutable**, allowing elements to be added or removed, while **frozensets** are immutable versions of sets.
4. Sets can be created using **set literals**, the `set()` constructor, or **set comprehensions** for concise generation.
5. **Dictionaries** store data as **key–value pairs**, where keys must be unique and immutable, while values can be of any type.
6. Dictionaries are **mutable and ordered by insertion (Python 3.7+)**, and support fast lookup, updating, deletion, and iteration over keys, values, or items.
7. Both sets and dictionaries are chosen based on use-case: sets for **uniqueness and membership testing**, dictionaries for **associating values with keys efficiently**.

# WEEK 8
1. All programs follow the **input → processing → output (I/O)** model, and I/O can involve users, files, networks, or other systems.
2. Python supports multiple ways to **format output**, with **f-strings** being the modern and recommended approach (Python 3.6+).
3. **Format specifiers** allow control over precision, width, alignment, padding, and number representation (e.g. decimal, binary, hexadecimal).
4. The `str.format()` method and older **`%`-style formatting** exist as alternatives, though f-strings are generally clearer and preferred.
5. **File handling** allows programs to read from and write to files, which may be treated as **text or binary** data.
6. Files must be **opened** using `open()` with the correct mode (`r`, `w`, `a`, `r+`, plus optional `b`) and **closed** after use.
7. The **`with` statement** is the safest way to work with files, ensuring they are automatically closed even if an error occurs.




