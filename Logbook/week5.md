
##  Summary 

When learning Python, using the interactive interpreter is helpful for testing ideas, but real programs are written in **text files** with a `.py` extension. These files are called **scripts** when they are executed directly. Scripts are run from the command line using the Python interpreter, and unlike interactive mode, they only display output when you explicitly use `print()`.

Scripts can also accept **command-line arguments**, which allow users to pass information into the program when it runs. These arguments are accessed using `sys.argv`, which stores them as a list of strings. This makes scripts flexible, since the same program can work with different inputs each time it runs.

A Python file doesn’t always have to be executed as a script. It can also be **imported as a module** into another program. Any `.py` file is considered a module, and importing it allows access to its functions, variables, and data types. When a module is imported, any top-level code inside it runs once, usually to perform setup or initialization.

There are **multiple ways to import modules**, and each affects how names are accessed. You can import an entire module, import specific items, or rename imports using aliases. Importing everything with a wildcard is possible, but discouraged because it can cause name conflicts and make code harder to understand.

Python uses a **module search path** to find modules when importing. This includes built-in modules, the current directory, paths set by the operating system, and any paths added at runtime.

To help inspect what a module contains, Python provides the `dir()` function, which is especially useful in interactive mode to explore available functions and variables.

Finally, the lecture introduces the special variable `__name__`, which allows a program to tell whether it is being **run directly** or **imported**. This makes it possible to write flexible code that works both as a standalone script and as a reusable module.

Overall, this lecture shows how Python programs are **structured, reused, and shared**, which is essential for building larger, real-world applications.


## Key Technologies 

### Program Files

* Python scripts (`.py` files)
* Plain text source files
* Interactive mode vs script execution

### Script Execution

* Running scripts from the command line
* Python interpreter
* Explicit output using `print()`

### Command-Line Arguments

* `sys.argv`
* Argument lists
* Converting string inputs to numbers

### Modules

* Python modules
* Reusable code
* Importing user-defined modules
* Module initialization code

### Import Mechanisms

* `import module`
* `import module as alias`
* `from module import name`
* `from module import name as alias`
* `from module import *` (discouraged)
* Namespace management
* Avoiding name clashes

### Module Search Path

* Built-in modules
* `sys.path`
* Current working directory
* `PYTHONPATH` environment variable
* Runtime path modification

### Introspection & Debugging

* `dir()` function
* Inspecting module contents
* Interactive exploration

### Script vs Module Detection

* `__name__` variable
* `__main__`
* Writing dual-purpose files (script + module)

