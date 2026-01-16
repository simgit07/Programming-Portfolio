
## Humad Summary

This lecture focuses on **Input/Output (I/O)** and **file handling**, which are essential parts of building real-world Python programs. Every program follows the basic pattern of **input → processing → output**, and while simple programs may rely on `input()` and `print()`, larger and more professional systems need more advanced I/O techniques.

We begin by improving **text output formatting**, learning how to control how information is displayed. Python provides several formatting approaches, with **f-strings** being the modern and most readable option. We also explore `str.format()`, manual formatting using string methods, and older `%`-style formatting so we can recognise legacy code.

The lecture then moves on to **file handling**, which allows programs to read data from files and write results back to files. We learn that all files are stored as bytes, but Python lets us treat them as either **text files** or **binary files**. To work with a file, we must open it using the `open()` function, specify an appropriate mode (read, write, append, etc.), and close it when finished.

We examine different ways to **read from files**, such as reading the entire file, reading line by line, or iterating directly over the file object. We also learn how to **write data** to files, noting that non-string data must be converted before writing.

Finally, we look at **file positions** and how Python keeps track of where we are within a file using `tell()` and `seek()`. The lecture emphasizes safe file handling using **exception handling** and the `with` statement, which automatically closes files even when errors occur.

---

## Key Technologies 

### Input / Output (I/O)

* Programs follow **input → processing → output**
* I/O is not limited to users; it includes files, networks, and devices
* `input()` and `print()` are basic I/O tools

---

### Output Formatting

* **F-strings (formatted string literals)**

  * Modern, readable, introduced in Python 3.6
  * Support expressions and format specifiers
* **Format specifiers**

  * Control precision, width, alignment, padding, and number base
  * Common uses: decimal places, column alignment
* **str.format()**

  * Older than f-strings but still valid
  * Supports positional and keyword arguments
* **Manual formatting**

  * `ljust()`, `rjust()`, `center()`, `zfill()`
* **%-style formatting**

  * Legacy formatting style
  * Useful for recognising older code

---

### File Handling

* Files are sequences of bytes (text or binary)
* Files must be **opened before use** and **closed after use**
* **Opening files**

  * `open(filename, mode)`
  * Common modes:

    * `r` (read), `w` (write), `a` (append), `r+` (read/write)
    * `b` suffix for binary files
* **Reading files**

  * `read()`, `readline()`, `readlines()`
  * Iteration using `for line in file`
* **Writing files**

  * `write()` (strings only)
  * Non-strings must be converted using `str()`

---

### File Position Control

* `tell()` → get current file position
* `seek()` → move file position

  * Relative to start (0), current (1), or end (2)

---

### Exception Handling & Safety

* File operations can fail and raise exceptions
* `try…except…finally` ensures files are closed
* **`with` statement**

  * Automatically closes files
  * Recommended best practice

